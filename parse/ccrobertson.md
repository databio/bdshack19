DATA=/Users/Cassie/bdshack19_data/sciCAR/rawdata/GSE117089_RAW/

#Obtain matching cell ids from mouse ATAC and RNA data sets
awk -v file=${DATA}/GSM3271044_RNA_mouse_kidney_cell.txt 'BEGIN {FS=","; while (getline<file) {a[$1]=1}} NR>1 && $1 in a {print $1}' ${DATA}/GSM3271045_ATAC_mouse_kidney_cell.txt > matching.txt
