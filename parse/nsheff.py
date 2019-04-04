import scipy
import scipy.io

scipy.io.mmread("/project/shefflab/bdshack")

a = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz")


g = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_gene_count.txt.gz")



# get dimensions with: 
a.shape
g.shape

import pandas
pks = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW//GSM3271045_ATAC_mouse_kidney_peak.txt.gz")


