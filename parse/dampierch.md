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

    zcat ${fn} | awk -v FS="," '{print $1}' | sort | uniq -c | less

__To find # fields in each file:__

    files=`find . -maxdepth 1 -name "*.txt.gz" | awk -v FS='/' '{print $2}'`
    for i in $files; do zcat $i | awk -v FS=',' -v n=$i 'NR==1 {print NF,n}' >> fields.txt; done

#### Key fields

For `GSM3271044_RNA_mouse_kidney_cell.txt.gz`:

$1,$3,$7::sample,replicate,cell_name

sample

    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort | uniq -c | awk '{print $1}' | sort | uniq -c

13,893 sample_ids

replicate

    zcat ${fn} | awk -v FS="," '{print $3}' | sort | uniq -c | less

6969 Replicate 1
6924 Replicate 2

cell_name

    zcat ${fn} | awk -v FS="," '{print $7}' | sort | uniq -c | less

15 cell types (including NA)

For `GSM3271045_ATAC_mouse_kidney_cell.txt.gz`:

$1,$2::sample,replicate

sample

    zcat ${fn} | awk -v FS="," '{print $1}' | sort | uniq -c | awk '{print $1}' | sort | uniq -c

13,395 sample_ids

replicate

    zcat ${fn} | awk -v FS="," '{print $2}' | sort | uniq -c | less

7049 Replicate 1
6346 Replicate 2

#### Cell annotations

From RNA-seq:

    fn=GSM3271044_RNA_mouse_kidney_cell.txt.gz
    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort > rna_sample_id.txt

From ATAC-seq:

    fn=GSM3271045_ATAC_mouse_kidney_cell.txt.gz
    zcat ${fn} | awk -v FS="," 'NR>1 {print $1}' | sort > atac_sample_id.txt

__Overlap:__

    awk 'NR==FNR {a[$0]; next} {for (i in a) if ($1==i) print $0}' rna_sample_id.txt atac_sample_id.txt

11,296 cells in both datasets

__Unique to RNA set:__

  ...cannot figure this out, switching to Python
    
__Unique to ATAC set:__

  ...cannot figure this out, switching to Python

#### Notes On All Fields

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
