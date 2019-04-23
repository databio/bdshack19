import logging
import os
import pandas as pd
import scanpy as sc
import scipy.io
import numpy as np

SUPPORTED_MODALITIES = ['RNA', 'ATAC', 'PROT']


class MultiAnnData(object):
    """
    Container for multiple measurement modalities, each represented as an AnnData object.
    
    Parameters
    ----------
    adatas : list of AnnData objects
        list of AnnData objects, each of which correspond to a different measurement modality.
    modalities : list of string
        list of strings specifying the modality of the measurements for each AnnData.

    Attributes
    ----------
    adatas : dict of string:AnnData
        dictionary mapping each modality to the AnnData object holding the data collected with that modality.
    
    """

    def __init__(self, modalities: str = None, adatas: str = None):

        self._adatas = {}

        if adatas and modalities:
            mode_map = dict(zip(modalities, adatas))
            for modality in mode_map.keys():
                self.add_modality(modality, mode_map[modality])

    def join(self, how, on, modalities=None):
        if not modalities:
            modalities = list(self._adatas.keys())
        if (len(modalities)) != 2:
            raise Exception("Must provide 2 modalities to join.")
        return pd.merge(self._adatas[modalities[0]].var,
                        self._adatas[modalities[1]].var, how=how, on=on)

    def load_modality(self, modality: str, file_x: str, file_obs: str = None, file_var: str = None,
                      obs_index: str = None, var_index: str = None, parent_folder: str = "",
                      transpose_x=False, overwrite=False):
        """
        Loads and adds a new modality
        """

        if modality not in SUPPORTED_MODALITIES:
            raise AttributeError("Unsupported modality: '{}'. Must be one of {}".format(
                modality, str(SUPPORTED_MODALITIES)))

        adata = load_AnnData(file_x, file_obs, file_var, obs_index, var_index, parent_folder,
                             transpose_x)

        self.add_modality(modality, adata, overwrite)

    def add_modality(self, modality: str, adata: sc.AnnData, overwrite=False):
        """ Adds an AnnData object to the MultiAnnData object """

        if modality not in SUPPORTED_MODALITIES:
            raise AttributeError('Unsupported modality. Must be one of ' + str(SUPPORTED_MODALITIES))

        if modality in self._adatas.keys():
            if not overwrite:
                raise AttributeError("Modality of type: {}, already exist in Multimeasure object".format(modality))
            else:
                logging.warn("Overwriting modality: {}".format(modality))

        self._adatas[modality] = adata

        print("Modality {} added.".format(modality))

    def is_empty(self):
        """ Check if object contains any modalities """
        return not bool(self._adatas)

    def save_modalities(self, file_name: str, select: list = None):
        """ Save selected modalities into .h5ad files.

        :param file_name: name of h5ad file
        :param select: list of modalities to save into separate files, if None all modalities will be saved
        """
        if not select:
            select = self._adatas.keys()

        for mtype in select:
            if mtype not in self._adatas.keys():
                raise AttributeError("Could not find {} modality".format(mtype))

        if file_name.lower().endswith(".h5ad"):
            file_name = file_name.split(".h5ad")[0]

        for mtype in select:
            self._adatas[mtype].write(file_name + "_" + mtype + ".h5ad")

    def __getattr__(self, name):
        """
        Allows for attribute-style access for supported modalities
        """
        if name in SUPPORTED_MODALITIES:
            return self._adatas[name]
        else:
            raise AttributeError("%r object has no attribute %r" %
                                 (self.__class__.__name__, name))

    def __getitem__(self, name):
        """
        Allows for attribute-style access for supported modalities
        """
        if name in SUPPORTED_MODALITIES:
            return self._adatas[name]
        else:
            raise KeyError("%r object has no item %r" %
                           (self.__class__.__name__, name))

    def __str__(self):

        str = "{} object with {} modalities\n".format(
            self.__class__.__name__, len(self._adatas))
        for k, v in self._adatas.items():
            str += "{key}: {val}\n".format(key=k, val=v.__str__())

        return str

    def has_modality(self, modality: str):
        """ Checks if object has modality of given type """
        return modality in self._adatas.keys()

    def intersection(self, first_type: str, second_type: str):
        """ Allows to finds common samples for two modalities.

        :param first_type: type of first modality
        :param second_type: type of second modality
        :return: two AnnData objects containing samples for both modalities (features are unchanged)
        """
        if not self.has_modality(first_type) or not self.has_modality(second_type):
            raise AttributeError("Could not find one/both of [{}, {}]  modalities.".format(first_type, second_type))
        mutual_cells = np.intersect1d(self[first_type].obs["sample"], self[second_type].obs["sample"])

        intersected = []
        for mtype in [first_type, second_type]:
            indices = [np.argwhere(self[mtype].obs["sample"] == x)[0, 0] for x in mutual_cells]
            matrix = self[mtype].X.tocsr()[indices, :]
            variables = self[mtype].var
            observation = self[mtype].obs.iloc[indices, :]
            intersected.append(sc.AnnData(X=matrix, obs=observation, var=variables))

        return intersected[0], intersected[1]

    def tSNE(self, modality_to_plot: str, modality_to_color: str, attribute: str, overwrite: bool = False,
             n_jobs: int = None):
        """ Plots t-SNE on selected modality colored by attribute from another modality

        :param modality_to_plot: type of modality chosen to plot
        :param modality_to_color: type of modality chosen to colors by
        :param attribute: attribute from modality_to_color
        :param overwrite: if FALSE use X_tsne attribute in modality_to_plot if available (otherwise X_tsne is calculated)
        :param n_jobs: number of jobs for tSNE
        :return: intersection of both modalities (AnnData object) with calculated X_tsne and attribute used for ploting
        """
        to_plot, to_color = self.intersection(modality_to_plot, modality_to_color)
        if attribute not in to_color.obs.columns.values:
            raise AttributeError("There is no {} attribute in {} modality".format())
        if 'X_tsne' not in to_plot.obsm.keys() or ('X_tsne' in to_plot.obsm.keys() and overwrite):
            if overwrite:
                logging.warning("X_tsne will be overwritten")
            logging.info("Calculating tSNE - it may take some time")
            sc.tl.tsne(to_plot, n_pcs=2, n_jobs=n_jobs)
        to_plot.obs.loc[:, attribute] = to_color.obs[attribute]
        sc.pl.tsne(to_plot, color=attribute)
        return to_plot

    #     sc.tl.tsne(self.measures[modality_type])
    #     self.measures[modality_type]
    # sc.settings.set_figure_params(dpi=150, dpi_save=600, frameon=True, vector_friendly=True, fontsize=10,
    #                                   color_map=None, format='svg')
    # sc.pl.scatter(self.measures[modality_type],
    #                   x='tsne_1', y='tsne_2', color='cell_name',
    #                   title='mouse kidney scRNA-based cell types',
    #                   legend_fontsize=7)


def load_AnnData(file_x: str, file_obs: str = None, file_var: str = None,
                 obs_index: str = None, var_index: str = None, parent_folder: str = "",
                 transpose_x=False):
    """
    Given up to 3 matrix files, creates AnnData file and adds it to Multimeasure object

    Parameters
    ----------
    file_x
        Filename for the data matrix itself (as a Matrix Market file).
    file_obs
        Filename for the observation annotation matrix in csv format.
    file_var
        Filename for variables annotation matrix in csv format.
    obs_index
        column label in obs for the column that should be assigned to the index. Optional,
        but required for plotting and some filtering with scanpy.
    var_index
        column label in var for the column that should be assigned to the index. Optional,
        but required for plotting and some filtering with scanpy.
    """

    X = sc.read_mtx(os.path.join(parent_folder, file_x))
    if transpose_x:
        X = X.transpose()

    if file_obs:
        obs = pd.read_csv(os.path.join(parent_folder, file_obs))
    else:
        obs = None

    if file_var:
        var = pd.read_csv(os.path.join(parent_folder, file_var))
    else:
        var = None

    X.obs = obs
    X.var = var

    if var_index:
        X.var_names = X.var[var_index].tolist()
    if obs_index:
        X.obs_names = X.obs[obs_index].tolist()

    return X

# parent_folder = "/Users/agatagruszczynska/PycharmProjects/2019hackathon/data"
# ad_rna = load_AnnData(
# 	"GSM3271044_RNA_mouse_kidney_gene_count.txt.gz",
# 	"GSM3271044_RNA_mouse_kidney_cell.txt.gz",
# 	"GSM3271044_RNA_mouse_kidney_gene.txt.gz",
# 	parent_folder=parent_folder, transpose_x=True)
# mad = MultiAnnData(["RNA"], [ad_rna])
# ad_atac = load_AnnData(
# 	"GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz",
# 	"GSM3271045_ATAC_mouse_kidney_cell.txt.gz",
#     "GSM3271045_ATAC_mouse_kidney_peak.txt.gz",
# 	parent_folder=parent_folder, transpose_x=True)
# mad = MultiAnnData(["ATAC", "RNA"], [ad_atac, ad_rna])
# mad.intersection("ATAC", "RNA")
