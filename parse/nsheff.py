import pandas
import scipy
import scipy.io

scipy.io.mmread("/project/shefflab/bdshack")


# peaks by cells
a = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz")

# genes by cells
g = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_gene_count.txt.gz")

# peaks annotation
pks = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_peak.txt.gz")


# genes annotation
genes = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_gene.txt.gz")

# cell annotations
gc = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_cell.txt.gz")

ac = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_cell.txt.gz")


a.shape
ac.shape

gc.shape
g.shape



