import os
import pandas as pd
import scanpy.api as sc
import numpy as np
import matplotlib.pyplot as plt

import scipy
import scipy.io

#export DATA=/Users/Cassie/bdshack19_data/sciCAR/rawdata/GSE117089_RAW/mouse/
#os.chdir(os.environ["DATA"])
os.chdir("/Users/Cassie/bdshack19_data/sciCAR/rawdata/GSE117089_RAW/mouse/")

### Create AnnData object
def createAnnDataObject(cell_file, feature_file, count_file, feature_name):

    #read in files
    cell = pd.read_csv(cell_file, sep = ',')
    feature = pd.read_csv(feature_file, sep = ',')
    count = scipy.io.mmread(count_file)

    # transpose to that each row corresponds to cell, each column corresponds to gene or peak
    adata_t = sc.AnnData(count.toarray())
    adata = sc.AnnData.transpose(adata_t)

    # set indices for obs and var
    cell.set_index('sample', inplace=True)
    feature.set_index(feature_name, inplace=True)

    adata.obs = cell
    adata.var = feature

    return adata
    

ad_RNA = createAnnDataObject(
    cell_file="GSM3271044_RNA_mouse_kidney_cell.txt",
    feature_file="GSM3271044_RNA_mouse_kidney_gene.txt",
    count_file="GSM3271044_RNA_mouse_kidney_gene_count.txt",
    feature_name="gene_id"
    )

ad_ATAC = createAnnDataObject(
    cell_file="GSM3271045_ATAC_mouse_kidney_cell.txt",
    feature_file="GSM3271045_ATAC_mouse_kidney_peak.txt",
    count_file="GSM3271045_ATAC_mouse_kidney_peak_count.txt",
    feature_name="peak"
    )

# ad_atac = load_AnnData(
# 	"GSM3271045_ATAC_mouse_kidney_peak_count.txt.gz",
# 	"GSM3271045_ATAC_mouse_kidney_peak.txt.gz",
# 	"GSM3271045_ATAC_mouse_kidney_cell.txt.gz",
# 	os.environ["DATA"], transpose_x=True)

#Look at distribution of cell counts
np.sum(ad_RNA.X, axis=0)[0:100]
np.histogram(np.sum(ad_RNA, axis=0)[0:100])

#FILTERING OUT ZERO CELLS/FEATURES
def filterData(ad, cell_count, prop_cells):
    
    #remove cells that have very few counts
    sc.pp.filter_cells(ad_RNA, min_counts=num_cells, inplace=True)
    
    #remove genes that aren't present in at least X% of cells
    prop_cells=0.2
    num_cells = int(prop_cells*ad_RNA.shape[0])
    sc.pp.filter_genes(ad_RNA, min_cells=num_cells, inplace=True)
    
    return ad




sc.pp.filter_cells(ad_RNA, min_counts=10, inplace=True)
ad_RNA.X.shape

sc.pp.calculate_qc_metrics(adata_RNA, inplace=True)
