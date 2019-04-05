====
MoPy
====

MoPy, short for MultiOmics Py, provides a new class of data object for single-cell multi-omics data analysis in Python. You will find it most useful for analysis of single-cell data generated from two or more separate omics modalities (e.g. RNA-seq, ATAC-seq). The class is built on AnnData objects from the Theis Lab. For single-modality analysis, the AnnData class and standard Scanpy functions will likely be more useful. Typical usage of MoPy often looks like this::

    #!/usr/bin/env python

    from mopy import multianndata

    if MultiAnnData():
        print "Your multi-omics-ready data object is stored in", #OBJECT NAME

API
===

The central class:

    class MultiAnnData(object)

Parameters
----------

Functions
=========

* First

* Second

Contributors
------------

Greg
Nathan
Etc

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. hi there

2. must be going

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.
