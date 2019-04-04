file name	description 

da.sites.csv	The ?peak? is the accessible site id including chromatin id, start position and end position separated by ?-?. For each cell type, significant score (p-value) was calculated for each sites comparing the cell type to other cells (Method). The ?cell_name? is the cell type name in comparison to other cell types. The ?qval? is the false detection rate in gene differential accessibility test across different cell types or treatment conditions. 

RNA_sciCAR_A549_cell.txt	Cell annotation file: sample is cell id of each single cell with the reverse transcription barcode attached; cell_name is the source of cells (293T, 3T3, A549); experiment is the experiment inforation: coassay (sci-CAR) or sci-RNA-seq only; treatment_time is the DEX treatment time for A549 cells (NA for other cell line). 

RNA_sciCAR_A549_gene.txt	Gene annotation file including gene id, gene typeand gene short name. 

RNA_sciCAR_A549_gene_count.txt	 A sparse matrix file: each row corresponds to gene id (with gene information in the df_gene_RNA; each column corresponds to each cell (with cell source information in the df_cell_RNA); each value in the matrix corresponds to UMI count.   

ATAC_sciCAR_A549_cell.txt 	Cell annotation file: sample is the cell id of each identified single cell with correlated reverse transcription barcode attached. For single cell ATAC-seq from sci-CAR, the sample id correlates with the sample id in the RNA_sciCAR_A549_cell.txt file; the source include cell source information (Human or Mouse); group include information about DEX treatment conition (A549_0h, A549_1h, A549_3h); experiment include the experiment information: ATAC_only (sci-ATAC-seq) or co-assay (sci-CAR ATAC-seq part) 

ATAC_sciCAR_A549_peak.txt	Peak annotation file including peak id, peak chromasom id, peak start coordinate, peak end coordinate.  

ATAC_sciCAR_A549_peak_count.txt	Sparse matrix file: each row corresponds to peak id (with peak information in the df_peak_ATAC; each column corresponds to each cell (with cell source information in the df_cell_ATAC); each value in the matrix corresponds to UMI count.   

RNA_only_A549_cell.txt	Cell annotation file: sample is cell id of each single cell with the reverse transcription barcode attached; cell_name is the source of cells (293T, 3T3, A549); experiment is the experiment inforation: coassay (sci-CAR) or sci-RNA-seq only; treatment_time is the DEX treatment time for A549 cells (NA for other cell line). 

RNA_only_A549_gene.txt	Gene annotation file including gene id, gene typeand gene short name. 

RNA_only_A549_gene_count.txt	 A sparse matrix file: each row corresponds to gene id (with gene information in the df_gene_RNA; each column corresponds to each cell (with cell source information in the df_cell_RNA); each value in the matrix corresponds to UMI count.   

ATAC_only_A549_cell.txt	Cell annotation file: sample is the cell id of each identified single cell with correlated reverse transcription barcode attached. For single cell ATAC-seq from sci-CAR, the sample id correlates with the sample id in the df_cell_RNA file in the RNA_A549.RData file; the source include cell source information (Human or Mouse); group include information about DEX treatment conition (A549_0h, A549_1h, A549_3h); experiment include the experiment information: ATAC_only (sci-ATAC-seq) or co-assay (sci-CAR ATAC-seq part) 

ATAC_only_A549_peak.txt 	Peak annotation file including peak id, peak chromasom id, peak start coordinate, peak end coordinate.  

ATAC_only_A549_peak_count.txt	Sparse matrix file: each row corresponds to peak id (with peak information in the df_peak_ATAC; each column corresponds to each cell (with cell source information in the df_cell_ATAC); each value in the matrix corresponds to UMI count.   

RNA_mouse_kidney_cell.txt	Cell annotation file: sample is cell id of each single cell with the reverse transcription barcode attached; replicateis the kidney replicate information (replicate 1 or replicate 2); experiment is the experiment inforation: coassay (sci-CAR) or sci-RNA-seq only. tsne_1 and tsne_2 are cell coordinates after t-SNE dimension reduction. cell_name include the annotated kidney cell type for each single cell. 

RNA_mouse_kidney_gene.txt	Gene annotation file including gene id, gene typeand gene short name. 

RNA_mouse_kidney_gene_count.txt	 A sparse matrix file: each row corresponds to gene id (with gene information in the df_gene_RNA; each column corresponds to each cell (with cell source information in the df_cell_RNA); each value in the matrix corresponds to UMI count.   

ATAC_mouse_kidney_cell.txt	Cell annotation file: sample is the cell id of each identified single cell with correlated reverse transcription barcode attached. For single cell ATAC-seq from sci-CAR, the sample id correlates with the sample id in the RNA_mouse_kidney_cell.txt file; replicate include the kidney replicate information (kidney replicate 1 or 2);experiment include the experiment information: ATAC_only (sci-ATAC-seq) or co-assay (sci-CAR ATAC-seq part). 

ATAC_mouse_kidney_peak.txt	Peak annotation file including peak id, peak chromasom id, peak start coordinate, peak end coordinate.  

ATAC_mouse_kidney_peak_count.txt	Sparse matrix file: each row corresponds to peak id (with peak information in the df_peak_ATAC; each column corresponds to each cell (with cell source information in the df_cell_ATAC); each value in the matrix corresponds to UMI count.   

Peak_CellType_signal.csv	Cell type consensus chromatin accessibility profiles (TPM, tags per million) in mouse kidney experiment 

