import logging
import os
import pandas as pd
import scanpy as sc
import scipy.io

SUPPORTED_MODALITIES = ['RNA', 'ATAC', 'PROT']


class MultiAnnData(object):
    """
    Container for multiple measurement modalities, each represented as an AnnData object.
    
    Parameters
    ----------
    measures : list of AnnData
        list of AnnData objects, each of which correspond to a different measurement modality.
    modalities : list of string
        list of strings specifying the modality of the measurements for each AnnData.

    Attributes
    ----------
    measures : dict of string:AnnData
        dictionary mapping each modality to the AnnData object holding the data collected with that modality.
    
    """

    def __init__(self, measures: str = None, modalities: str = None):

        # Initiate attributes for supported modalities
        for modality in SUPPORTED_MODALITIES:
            setattr(self, modality, None)

        self.measures = {}
        if measures and modalities:
            mode_map = dict(zip(modalities, measures))
            for modality in mode_map.keys():
                if modality not in SUPPORTED_MODALITIES:
                    raise AttributeError('Unsupported modality. Must be one of ' + str(SUPPORTED_MODALITIES))
                self.measures[modality] = mode_map[modality]
                setattr(self, modality, mode_map[modality])

    def __str__(self):

        str = "{} object with {} modalities\n".format(
            self.__class__.__name__, len(self.measures))
        for k, v in self.measures.items():
            str += "{key}: {val}\n".format(key=k, val=v.__str__())

        return str

    def join(self, how, on, modalities=None):
        if not modalities:
            modalities = list(self.measures.keys())
        if (len(modalities)) != 2:
            raise Exception("Must provide 2 modalities to join.")
        return pd.merge(self.measures[modalities[0]].var,
                        self.measures[modalities[1]].var, how=how, on=on)

    def add_modality(self, modality: str, file_x: str, file_obs: str = None, file_var: str = None,
                    obs_index: str = None, var_index: str = None, parent_folder: str = "", 
                     transpose_x=False, overwrite=False):
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

        if modality not in SUPPORTED_MODALITIES:
            raise AttributeError('Unsupported modality. Must be one of ' + str(SUPPORTED_MODALITIES))

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

        if modality in self.measures.keys():
            if not overwrite:
                raise AttributeError("Modality of type: {}, already exist in Multimeasure object".format(modality))
            else:
                logging.warn("Overwriting modality: {}".format(modality))

        X.obs = obs
        X.var = var
        
        if var_index:
            X.var_names = X.var[var_index].tolist()
        if obs_index:
            X.obs_names = X.obs[obs_index].tolist()
        
        self.measures[modality] = X
        
        setattr(self, modality, self.measures[modality])
        print("Modality {} added.".format(modality))

    def is_empty(self):
        """ Check if object contains any modalities """
        return not bool(self.measures)

    def save_modalities(self, file_name: str, select: list = None):
        """ Save selected modalities into .h5ad files.

        :param file_name: name of h5ad file
        :param select: list of modalities to save into separate files, if None all modalities will be saved
        """
        if not select:
            select = self.measures.keys()

        for mtype in select:
            if mtype not in self.measures.keys():
                raise AttributeError("Could not find {} modality".format(mtype))

        if file_name.lower().endswith(".h5ad"):
            file_name = file_name.split(".h5ad")[0]

        for mtype in select:
            self.measures[mtype].write(file_name + "_" + mtype + ".h5ad")
