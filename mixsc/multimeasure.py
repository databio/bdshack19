
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
            