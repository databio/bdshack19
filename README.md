# BDS Hackathon 2019



## Schedule

Date/Time: Apr 4th 9am - Apr 5th (midnight)

Room: TBD

See [2017 BDS hackathon](https://github.com/databio/bds_hackathon).

## Overview

During this hackathon we seek to develop a new python package that will load, store, visualize, and analyze single-cell multi-omic datasets produced from [CITE-seq](https://www.nature.com/nmeth/journal/v14/n9/full/nmeth.4380.html) or pi-ATAC experiments. 

## Outline of the deliverable

Our python package will need to accomplish these tasks:

### Packaging structure
Making  our functions installable, distributable.

- look at cookie cutter
- could use as a template existing packages from group members: e.g. [medusa](https://github.com/gregmedlock/Medusa), [peppy](http://github.com/databio/peppy), [divvy](http://github.com/databio/divvy)
- submit to pypi?

### parsing

How do we load up sample metadata?

- possibly use [PEP structure](http://pepkit.github.com) using [peppy](http://github.com/databio/peppy).

### Python object

We should produce a python object that implements data structures for this data type. Can we re-use existing tools?

### Visualization

We should produce a series of functions on our object that visualize the data in different ways.

### Machine learning

Object functions should make and return predictions. Can possible re-use ideas from the 2017 hackathon.


## Compute organization

Each of you should be a member of the `bds_tg` group on Rivanna. We have an allocation of disk space on Rivanna at `/sfs/lustre/allocations/bds_tg`. Set an environment variable to point to this for easy communication:

```
export BDSDATA="/sfs/lustre/allocations/bds_tg"
```

You should also have access to a compute credit allocation, also called `bds_tg` (use `allocations` to see yours).

Please commit any code into this repository.



## Data
* [GEO Data from Stoeckius 2017](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100866)

Cell Hashing (adds sample identity barcodes to CITEseq, for a total of 3 modalities)
paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6300015/
data: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE108313
(this one seems like it has less ADTs than the original CITEseq's ~13 ADTs, since it was more focused on optimizing titrations)

ECCITEseq (adds CRISPR sgRNA & VDJ clonality on top of Cell Hashing, for a total of 5 modalities)
paper: https://www.biorxiv.org/content/biorxiv/early/2018/11/08/466466.full.pdf
data: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126310
(missing some patient raw sequence data, since those are being submitted to dbGAP for privacy... but the count tables are available)
(this one has ~49 ADTs)

## Resources
