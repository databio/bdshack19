import pandas as pd
import scipy
import scipy.io
import os

parent_folder = "/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/"

ad_atac = load_AnnData(
	"GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz", 
	"GSM3271045_ATAC_mouse_kidney_peak.txt.gz",
	"GSM3271045_ATAC_mouse_kidney_cell.txt.gz",
	parent_folder, transpose_x=True)

ad_rna = load_AnnData(
	"GSM3271044_RNA_mouse_kidney_gene_count.txt.gz", 
	"GSM3271044_RNA_mouse_kidney_cell.txt.gz",
	"GSM3271044_RNA_mouse_kidney_gene.txt.gz",
	parent_folder, transpose_x=True)

mm = Multimeasure([ad_atac, ad_rna], ["ATAC", "RNA"])

mm.measures['ATAC'].X.shape

# linking two modalities:
merge = mm.join(how="inner", on="sample")
merge.iloc[1:5,:]
merge.shape



merge = mm.join(how="outer", on="sample")



pd.merge(ac, gc, how="outer", on="sample")
pd.merge(ac, gc, how="inner", on="sample").iloc[1:5,:]
















# Deprecated code


# Data matrices
# peaks by cells
a = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz")

# genes by cells
g = scipy.io.mmread("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_gene_count.txt.gz")

# Column annotations (feature annotation)
# peaks annotation
pks = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_peak.txt.gz")

# genes annotation
genes = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_gene.txt.gz")

# Row annotation (cell annotation)
# cell annotations
ac = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_cell.txt.gz")

gc = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_cell.txt.gz")

