
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
        str = "{} object\n".format(self.__class__.__name__)
        str += "{} data types\n".format(len(self.measures))
        for k,v in self.measures.items():
            str += "{key}: {val}\n".format(key=k, val=v.__str__())

        return str




def load_AnnData(file_x, file_obs, file_var, parent_folder=None):
    """
    Given 3 matrices, returns an anndata object. Helps for
    loading annData objects.
    """
    X = scipy.io.mmread(os.path.join(parent_folder, file_x))
    obs = pandas.read_csv(os.path.join(parent_folder, file_obs))
    var = pandas.read_csv(os.path.join(parent_folder, file_var))
    return(AnnData(X=a, obs=pks, var=ac))
