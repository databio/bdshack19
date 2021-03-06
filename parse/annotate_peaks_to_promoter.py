import pybedtools as pybed
import pandas as pd

def get_TSS( row ):
	row_strand = row['strand']
	row_start = row['start']
	row_end = row['end']
	if( row_strand == "+" ):
		return row_start 
	else:
		return row_end

## Function to annotate peaks to promoter region
## Takes input : a gff file ( gff3 format ) ; a dataframe similar to bed file with peaks.
def annotate_peaks_to_promoter( gff , peaks ):
	
	# Parse gff to get promoter regions ( TSS +/- 500 )
	## 1) First few lines of the GFF file start with "#" -> remove these 
	## 2) Retain only gene_id and gene_name from the annotation field
	## 3) TSS annotation -> for "+" strand , TSS is transcript_start , for "-" strand , TSS is transcript_end 
	## 4) Finally , convert the dataframe to bedtools object

	gff_pd = pd.read_csv( gff , sep = "\t" , names = ["chr" , "chrAnnot", "region" , "start" , "end" , "score" , "strand" , "score1" , "annotation" ] )
	gff_pd = gff_pd[ ( gff_pd['region'] == "transcript" ) & ( ~ gff_pd ['chr'].astype(str).str.startswith('#') ) ]
	gff_pd['gene_id'] = gff_pd['annotation'].apply( lambda x : re.sub( 'gene_id=' , '' , "".join( [k for k in x.split(";") if 'gene_id=' in k] ) ) )
	gff_pd['gene_name'] = gff_pd['annotation'].apply( lambda x : re.sub( 'gene_name=' , '' , "".join( [k for k in x.split(";") if 'gene_name=' in k] ) ) )
	gff_pd = gff_pd.drop('annotation', 1)

	promoter = gff_pd
	promoter['TSS'] = spromoter.apply( get_TSS , axis = 1 )
	promoter = gff_pd[[ 'chr' , 'start' , 'end' , 'strand' , 'gene_id' , 'gene_name' , 'TSS' ]]
	promoter['TSS'] = promoter.apply( get_TSS , axis = 1 )
	promoter['start'] = promoter['TSS'] - 500 
	promoter['end'] = promoter['TSS'] + 500 
	promoter = pybed.BedTool.from_dataframe( promoter )

	peaks = pybed.BedTool.from_dataframe( peaks )

	# Intersecting peaks with the promoter regions 
	intersectRes = peaks.intersect( promoter ,wao=True )

	# Convert the intersectRes object to pandas data frame 
	intersectRes_pd = pd.read_csv( intersectRes.fn , sep = "\t" , names = ["peak_chr", "peak_start", "peak_end", "chr" ,	"chrAnnot"	, "region"	, "start" , "end",	"score" , "strand"	, "score1" , "gene_id"	, "gene_name", "TSS" , "amount_of_overlap"] )
	# Filter for atleast 1bp overlap
	intersectRes_pd[ intersectRes_pd[ 'amount_of_overlap'] >= 1 ]

  return intersectRes_pd
  
  
# in the main : use this 
gff = "/sfs/lustre/allocations/shefflab/bdshack19/sciCAR/refgenome/gencode.vM11.annotation.gff3"
annotatedPeaks = annotate_peaks_to_promoter( gff , peaks )
