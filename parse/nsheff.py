import pandas
import scipy
import scipy.io

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

# linking two modalities:

pd.merge(ac, gc, how="outer", on="sample")
pd.merge(ac, gc, how="inner", on="sample").iloc[1:5,:]




class TripleMatrix(object):
	"""
	Representation of a single modality

	It's made of 3 matrices: A data matrix, a column annotation
	matrix, and a row annotation matrix.
	"""
	def __init__(self, data, cell_anno, feature_anno):
		self.data = data
		self.cell_anno = cell_anno
		self.feature_anno = feature_anno



class SSMultiHolder(object):
	"""
	Holds multiple modalities
	"""
	def __init__(self, modality_list):
		"""
		:param modality_list list[TripleMatrix]: A list of data objects containing information about each modality.
		"""
		print("Hello!")



	def update_feature_annotation(self, features):
		"""
		Updates feature annotation matrix
		"""

