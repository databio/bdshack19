import pandas
import scipy
import scipy.io

scipy.io.mmread("/project/shefflab/bdshack")


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
gc = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271044_RNA_mouse_kidney_cell.txt.gz")

ac = pandas.read_csv("/project/shefflab/bdshack19/sciCAR/rawdata/GSE117089_RAW/GSM3271045_ATAC_mouse_kidney_cell.txt.gz")


a.shape
ac.shape

gc.shape
g.shape

tm_genes = TripleMatrix(g, gc, genes)
tm_atac = TripleMatrix(a, ac, pks)



class TripleMatrix(object):

	def __init__(self, data, cell_anno, feature_anno):
		self.data = data
		self.cell_anno = cell_anno
		self.feature_anno = feature_anno



class SSMultiHolder(object):

	def __init__():
		print("Hello!")



	def update_feature_annotation(self, features):
		"""
		Updates feature annotation matrix
		"""

