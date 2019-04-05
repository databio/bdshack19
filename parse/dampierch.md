# sciCAR Dataset Parser

Start in `/sfs/lustre/allocations/shefflab/bdshack19/sciCAR`.

## Raw Data

Find raw data in `/sfs/lustre/allocations/shefflab/bdshack19/sciCAR/rawdata`.

### Explore

I start with `awk` because I know how to use it. I want to learn how to do this in `Python`.

First two lines of `GSM3271044_RNA_mouse_kidney_cell.txt.gz`:

    $fn=GSM3271044_RNA_mouse_kidney_cell.txt.gz
    $zcat ${fn} | awk -v FS="," 'NR<3 {print $0}'

    sample,source,replicate,experiment,tsne_1,tsne_2,cell_name
    coRNA-RNA-plate1-001.TCGGCGTCGT,Mouse,Replicate 1,coassay,NA,NA,NA

To see all the sample_ids and their frequency:

    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort | uniq -c | less

__To find # fields in each file:__

    files=`find . -maxdepth 1 -name "*.txt.gz" | awk -v FS='/' '{print $2}'`
    for i in $files; do zcat $i | awk -v FS=',' -v n=$i 'NR==1 {print NF,n}' >> fields.txt; done

### Key fields

For `GSM3271044_RNA_mouse_kidney_cell.txt.gz`:

    fn=GSM3271044_RNA_mouse_kidney_cell.txt.gz

$1,$3,$7::sample,replicate,cell_name

*sample*

    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort | uniq -c | awk '{print $1}' | sort | uniq -c

__13,893__ sample_ids

*replicate*

    zcat ${fn} | awk -v FS="," 'NR>1 {print $3}' | sort | uniq -c | less

__6,969__ Replicate 1
__6,924__ Replicate 2

*cell_name*

    zcat ${fn} | awk -v FS="," 'NR>1 {print $7}' | sort | uniq -c | less | wc -l

__15__ cell types (including NA)

For `GSM3271045_ATAC_mouse_kidney_cell.txt.gz`:

    fn=GSM3271045_ATAC_mouse_kidney_cell.txt.gz

$1,$2::sample,replicate

*sample*

    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort | uniq -c | awk '{print $1}' | sort | uniq -c

__13,395__ sample_ids

*replicate*

    zcat ${fn} | awk -v FS="," 'NR>1 {print $2}' | sort | uniq -c | less

__7,049__ Replicate 1
__6,346__ Replicate 2

### Cell annotations

#### From RNA-seq

    fn=GSM3271044_RNA_mouse_kidney_cell.txt.gz
    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort > rna_sample_id.txt

#### From ATAC-seq

    fn=GSM3271045_ATAC_mouse_kidney_cell.txt.gz
    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort > atac_sample_id.txt

#### Overlap

    awk 'NR==FNR {a[$0]; next} {for (i in a) if ($1==i) print $0}' rna_sample_id.txt atac_sample_id.txt

__11,296__ cells in both datasets

Cassie's version is way faster:

    awk -v file=${DATA}/GSM3271044_RNA_mouse_kidney_cell.txt 'BEGIN {FS=","; while (getline<file) {a[$1]=1}} NR>1 && $1 in a {print $1}' ${DATA}/GSM3271045_ATAC_mouse_kidney_cell.txt > matching.txt

I modify my code to be faster:

    awk -v FS="," 'NR==FNR {a[$1]; next} {if ($1 in a) print $1}' GSM3271040_RNA_sciCAR_A549_cell.txt GSM3271041_ATAC_sciCAR_A549_cell.txt | wc -l

#### Unique to RNA set

    awk -v FS="," 'NR==FNR {a[$1]; next} {if (!($1 in a)) print $1}' GSM3271041_ATAC_sciCAR_A549_cell.txt GSM3271040_RNA_sciCAR_A549_cell.txt | wc -l

__1,268__ cells only in RNA set

*I think this number is incorrect, because total RNA ids minus total overlap ids is 2597. Something is missing. I will ignore this for now because it's irrelevant to larger project.*

#### Unique to ATAC set

    awk -v FS="," 'NR==FNR {a[$1]; next} {if (!($1 in a)) print $1}' GSM3271040_RNA_sciCAR_A549_cell.txt GSM3271041_ATAC_sciCAR_A549_cell.txt | wc -l

__1,260__ cells only in ATAC set

*I think this number is incorrect, because total ATAC ids minus total overlap ids is 2099. Something is missing. I will ignore this for now because it's irrelevant to larger project.*

### Notes

sample
zcat ${fn} | awk -v FS="," '{print $1}' | sort | uniq -c | awk '{print $1}' | sort | uniq -c
13,893 sample_ids

source
zcat ${fn} | awk -v FS="," '{print $2}' | sort | uniq -c | less
13,893 mouse

replicate
zcat ${fn} | awk -v FS="," '{print $3}' | sort | uniq -c | less
6969 Replicate 1
6924 Replicate 2

experiment
zcat ${fn} | awk -v FS="," '{print $4}' | sort | uniq -c | less
13,893 coassay

tsne_1
zcat ${fn} | awk -v FS="," '{print $5}' | sort | uniq -c | less
10728 tsne_1 values occur a single time
a single tsne value (NA) occurs 3166 times

tsne_2
zcat ${fn} | awk -v FS="," '{print $6}' | sort | uniq -c | less
10728 tsne_2 values occur a single time
a single tsne value (NA) occurs 3166 times

cell_name
zcat ${fn} | awk -v FS="," '{print $7}' | sort | uniq -c | less
74 Active proliferating cells (Ki-67+)
 1 cell_name
219 Collecting  duct intercalated  cells
958 Collecting  duct  principal  cells
764 Distal convoluted tubule cells
972 Endothelial cells
1282 Loop of Henle cells
230 Medullary collecting duct cells
3166 NA
86 Paranephric body adipocyte
104 Podocyte
2358 Proximal tubule S1/S2 cells
2136 Proximal tubule S3 cells (type 1)
1009 Proximal tubule S3 cells (type 2)
344 Renal pericytes
191 Stem cells (Kit+)
