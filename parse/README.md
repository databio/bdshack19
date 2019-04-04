# Parse and Create Python Data Object

In this part of the project, we parse the semi-processed GEO data from GSE117089 (the sciCAR raw dataset). We take as inputs a set of text files downloaded from GEO. We generate as output a Loom file that `scanpy` can subsequently read in as a data object for downstream manipulation and analysis.

## Description of observed text input files

`*_cell.txt.gz`: each row is individual cell identifier with information about whether it is replicate 1 or replicate 2

## Proposal for desired loom output file

## Major steps

* Link single-cell annotations with gene (for RNA-seq) and peak (for ATAC-seq) measurements
* Convert sparse matrix to "dense" matrix

### Link annotations with measurements

### Convert sparse matrix
