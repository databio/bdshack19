import pybedtools as pybed
import pandas as pd

gff = "/sfs/lustre/allocations/shefflab/bdshack19/sciCAR/refgenome/gencode.vM11.annotation.gff3"
# 'bed' file is the last 3 columns from this file - GSM3271043_ATAC_only_A549_peak.txt 
bed = "/home/yn9w/hackathon/GSM3271043_ATAC_only_A549_peak_simplified.txt"

peaks = pybed.BedTool(bed)
intersectRes = peaks.intersect(gff,wao=True)

## intersectRes would like this -
#chr1	3206300	3206564	chr1	HAVANA	exon	3205901	3207317	.	-	.	ID=exon:ENSMUST00000162897.1:2;Parent=ENSMUST00000162897.1;gene_id=ENSMUSG00000051951.5;transcript_id=ENSMUST00000162897.1;gene_type=protein_coding;gene_status=KNOWN;gene_name=Xkr4;transcript_type=processed_transcript;transcript_status=KNOWN;transcript_name=Xkr4-003;exon_number=2;exon_id=ENSMUSE00000866652.1;level=2;transcript_support_level=1;havana_gene=OTTMUSG00000026353.2;havana_transcript=OTTMUST00000086625.1
#chr1	3206300	3206564	chr1	HAVANA	exon	3206523	3207317	.	-	.	ID=exon:ENSMUST00000159265.1:2;Parent=ENSMUST00000159265.1;gene_id=ENSMUSG00000051951.5;transcript_id=ENSMUST00000159265.1;gene_type=protein_coding;gene_status=KNOWN;gene_name=Xkr4;transcript_type=processed_transcript;transcript_status=KNOWN;transcript_name=Xkr4-002;exon_number=2;exon_id=ENSMUSE00000867897.1;level=2;transcript_support_level=1;havana_gene=OTTMUSG00000026353.2;havana_transcript=OTTMUST00000086624.1
#chr1	3206300	3206564	chr1	HAVANA	transcript	3205901	3216344	.	-	.	ID=ENSMUST00000162897.1;Parent=ENSMUSG00000051951.5;gene_id=ENSMUSG00000051951.5;transcript_id=ENSMUST00000162897.1;gene_type=protein_coding;gene_status=KNOWN;gene_name=Xkr4;transcript_type=processed_transcript;transcript_status=KNOWN;transcript_name=Xkr4-003;level=2;transcript_support_level=1;havana_gene=OTTMUSG00000026353.2;havana_transcript=OTTMUST00000086625.1
#chr1	3206300	3206564	chr1	HAVANA	transcript	3206523	3215632	.	-	.	ID=ENSMUST00000159265.1;Parent=ENSMUSG00000051951.5;gene_id=ENSMUSG00000051951.5;transcript_id=ENSMUST00000159265.1;gene_type=protein_coding;gene_status=KNOWN;gene_name=Xkr4;transcript_type=processed_transcript;transcript_status=KNOWN;transcript_name=Xkr4-002;level=2;transcript_support_level=1;havana_gene=OTTMUSG00000026353.2;havana_transcript=OTTMUST00000086624.1

## Convert to pandas data frame 
intersectRes_pd = pd.read_csv( intersectRes.fn , sep = "\t" , names = ["peak_chr", "peak_start", "peak_end", "chr" , "start", "end" , "coverage" , ""] )
