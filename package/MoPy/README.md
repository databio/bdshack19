# MoPy

[MoPy](https://github.com/databio/bdshack19/tree/master/package/MoPy) (aka MadPy), short for MultiOmics in Python, (and a temporary substitute for MadPy until that name is made available to us), provides a new class of data object for single-cell multi-omics data analysis in [Python](https://www.python.org/). You will find it most useful for analysis of two or more separate omics modalities (e.g. RNA-seq, ATAC-seq) generated coincidently from single cells. The class is built on [AnnData objects](https://anndata.readthedocs.io/en/latest/) from the [Theis Lab](https://github.com/theislab). For single-modality analysis, the established [anndata.AnnData](https://anndata.readthedocs.io/en/latest/anndata.AnnData.html#anndata.AnnData) class and standard [Scanpy](https://scanpy.readthedocs.io/en/stable/) functions will likely be more useful. Typical usage of [MoPy](https://github.com/databio/bdshack19/tree/master/package/MoPy) (aka MadPy) often looks like this:

    #!/usr/bin/env python

    from mopy import multianndata

    if MultiAnnData():
        print "Your multi-omics-ready data object is stored in", #OBJECT NAME

## API

The central class:

    class MultiAnnData(object)

### Parameters

* List of parameters here
* Second item in list

## Functions

* First
* Second

## Contributors

* Greg
* Nathan
* Etc
