#Obtain matching cell ids from mouse ATAC and RNA data sets
awk -v file=GSM3271044_RNA_mouse_kidney_cell.txt 'BEGIN {FS=","; while (getline<file) {a[$1]=1}} $1 in a {print $1}' GSM3271045_ATAC_mouse_kidney_cell.txt > matching.txt
