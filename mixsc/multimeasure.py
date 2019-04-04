import pandas as pd

SUPPORTED_MODALITIES = ['RNA', 'ATAC', 'PROT_QUANT']

class Multimeasure(object):
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
    
    def __init__(self, measures, modalities):
        
        self.measures = {}
        mode_map = dict(zip(modalities,measures))
        for modality in mode_map.keys():
            if modality not in SUPPORTED_MODALITIES:
                raise AttributeError('Unsupported modality. Must be one of ' + str(SUPPORTED_MODALITIES))
            self.measures[modality] = mode_map[modality]
            

    def __str__(self):
        str = "{} object with {} modalities\n".format(
            self.__class__.__name__), len(self.measures))
        for k,v in self.measures.items():
            str += "{key}: {val}\n".format(key=k, val=v.__str__())

        return str


    def join(self, how, on, modalities=None):
        if not modalities:
            modalities = list(self.measures.keys())
        if (len(modalities)) != 2:
            raise Exception("Must provide 2 modalities to join.")
        return pd.merge(mm.measures[modalities[0]].var, 
            mm.measures[modalities[1]].var, how=how, on=on)




def load_AnnData(file_x, file_obs=None, file_var, parent_folder=None, transpose_x=False):
    """
    Given 3 matrices, returns an anndata object. Helps for
    loading annData objects.

    :param file_x: Filename for the data matrix itself (as a MM)
    :param file_obs: Filename for the observation annotation matrix in csv format
    :param file_var: Filename for variables annotation matrix in CSV format.
    """
    X = scipy.io.mmread(os.path.join(parent_folder, file_x))
    if transpose_x:
        X = X.transpose()
    
    if file_obs:
        obs = pandas.read_csv(os.path.join(parent_folder, file_obs))
    else:
        obs = None

    if file_var:
        var = pandas.read_csv(os.path.join(parent_folder, file_var))
    else:
        var = None

    return(AnnData(X=X, obs=obs, var=var))
