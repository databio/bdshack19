# BDS Hackathon 2019

### About
The __Biomedical Data Sciences Training Program__ ([bds_tg](http://bme.virginia.edu/bds/)) is organizing a 2nd annual hackathon for April 4-5, 2019. This will be a 48-hour event nucleated by the current trainees on the Biomedical Data Science NIH T32 training grant, and will be open to other interested participants. Food will be provided to those who have RSVP'd to fuel a collaborative and productive 48 hours. 

Last year, the [prior hackathon](https://github.com/databio/bds_hackathon) analyzed the CITEseq dataset (one of the first multi-omic single-cell datasets) and presented their efforts at the annual [UVA Datapalooza](https://www.youtube.com/watch?v=6qDEeRsMv7s&t=3808s). 

__This year__, we will apply collective skillsets of all attendees towards analyzing __single-cell resolution multi-omic data__, with the aim of producing a __python package__ that will automate aspects of analyzing this increasingly popular data type. 

#### No previous skills are required to attend, but just one of any of the following could be helpful:
 - working knowledge of R or python in data wrangling or package development
 - some experience with statistical or machine learning libraries/packages
 - working knowledge of either cytometry or sequencing data types
 - working knowledge of mouse/human cell types and common biomarkers used for their identification or functional readout
 - experience with optimizing visualization and/or graphical design

Feel free to share this announcement with individuals you think might be interested in participating!

#### Expectations:
 - have fun and make friends!
 - come with an appetite to learn, regardless of how advanced you may be in a particular area
 - embrace working together (you might temporarily go faster alone, but in the long run you'll only go farther as a team)
 - share your skills
   - teach others and be patient with those learning for the first time
   - the act of teaching forces you to synthesize your strategy and helps you (re)consider why you're doing something
 - ask questions (there are no stupid questions!)
   - in addition to what or how, ask each other WHY are you doing this? you may be surprised to find that it could lead to better ways of doing something, which may be especially clear when you're forced to remove the jargon and distill the main idea to a colleague



---

## Logistics
 
### Date/Time
Thu Apr 4th 9am - Fri Apr 5th midnight

### Location(s)
[Rice Hall](https://goo.gl/maps/TRenTumyx3P2) (computer science building)
 - if you have trouble getting in or finding your way, feel free to email organizers, or post in the slack channel (someone might be already there and can let you in)
 - __Room 128__, main room for both days (except Fri noon-2pm)
 - __Room 242__, lunch both days: noon-2pm
Breakout groups feel free to spillover into lounge areas around Rice Hall, or elsewhere. 

After the dedicated 2-day hackathon concludes, we will aim to present the work to a broader audience (scheduling with [CvilleBioHub](https://cvillebiohub.org/) some time in ~May).

### Live Chat
Post questions or chat with team members here:
 - sign up or go to UVACompBio's [`#hackathon2019` Slack channel](https://uvacompbio.slack.com/messages/CHGLT0XMK/)

Share on Twitter: UVa BDS [@uva_biodatasci](https://twitter.com/uva_biodatasci)

#### 2019 Organizers:
 - Nathan Sheffield (ns5bc), [website](http://databio.org/)
 - Gregory Medlock (glm5uh), prior bdstg trainee
 - Jeffrey Xing (jcx9dy), prior bdstg trainee

#### Oversight:
Make sure to thank Jason and Kim for making this possible, and feeding you!
 - Jason Papin (jap8r)
 - Kimberly Fitzhugh-Higgins (kaf5r)

---

## Outline of the deliverable

During this hackathon we seek to develop a new python package (taking advantage of existing tools where available) that will load, store, visualize, and analyze single-cell multi-omic datasets from a recently published dataset (see below). 

Our python package will need to consider and implement these elements:

### Packaging structure
Making our functions installable and easily distributable would lead to convenient usage by others. Organizers can help here, when we get to this point!

Can take a look at cookie cutter examples/templates to guide initial development:
- could use as a template existing packages from group members: e.g. [medusa](https://github.com/gregmedlock/Medusa), [peppy](http://github.com/databio/peppy), [divvy](http://github.com/databio/divvy)
- submit to pypi? conda?
- documentation? readthedocs? vs others?

### Parsing

What data types will we work with? 
 - Are these measured as part of the experiment, or referenced from other sources/databases? (e.g. metadata, reference data)
 - What are their sizes, formats, etc?
 - How do we load up sample data and metadata?
   - possibly use [PEP structure](https://pepkit.github.io) using [peppy](https://code.databio.org/peppy/).
 - What do other scRNAseq tools use? How are (will) new modalities (be) handled?

### Python object

Thinking about input/output as well as manipulating the data (in RAM, on disk):
 - How should the data be stored/manipulated? (e.g. a python object that implements data structures for this data type)
 - Can we re-use existing tools or object data structures?
 - How abstract should the object(s) be? How should components be organized relative to each other or in modules?

### Visualization

Visuals are fundamentally a key aspect of human communication and information exchange (highest bandwidth sensory modality, not to mention the backbone of scientific publications or presentations). A good visual at any step of the analysis should be useful for summarizing and/or communicating your ideas or findings. 

How should the data be visualized?
 - What questions would scientists, biologists, physicians want to ask of the data? 
 - What visuals would be biologically meaningful/useful? 
 - Which visuals are most suited for which datatype? Are any generalizable across modalities/datatypes? 
 - Are there ways to make the human ingestion of this information more efficient/practical? (e.g. as data size dimension/complexity/samples grow, the human reader will be limited in ability to scan through too many plots)
 - How should we accomplish these? (e.g. python functions in the object)

Bonus: if combined with interactive tools, a "tactile" dimension can be added to the data visualization, enabling "hands-on" exploration

### Machine learning

"Machine learning" is a general word that may mean different things to different people. Technically, it includes both supervised (useful to make predictions) and unsupervised (useful for exploring unknowns without prior assumptions) strategies, or combinations of these; and may range from simple algorithms like linear regression (fitting a line to some points) to fancier/newer algorithms like deep neural networks running on GPUs. 

Before going down the rabbit hole of which tools to utilize/wrangle in a 2-day time window, start by considering:
 - How do you know your data is good? What quality control measures would reassure you before proceeding at each step?
 - How would you want to __analyze__ the data? 
   - What kind of data is it? What can you do with it? 
   - What would biologically/scientifically be meaningful or useful? 
 - If it's possible to make predictions, what kinds of predictions would be useful to make from these data? How should they be made? 
 - What external information is useful to pair with this data? How can they be "integrated" in or leveraged at various steps?

Checking some published papers, or existing documentation in various tools may serve as inspiration for some of these questions.

---

## Data

#### Option 1. pi-ATAC (ATAC + protein)
paper (Chen 2018): https://www.nature.com/articles/s41467-018-07115-y

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE112091
 - ATAC-seq with 168 single cells from GM12878 cell line
 - 

#### Option 2. CITE-seq (RNA + protein)
paper (Stoeckius 2017): https://www.nature.com/nmeth/journal/v14/n9/full/nmeth.4380.html

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100866
 - 13 cellular surface markers (via ADTs)

Pros:
 - same dataset analyzed in last year's hackathon; at some of the participants will already be familiar with the dataset
 - potentially faster learning curve
Cons: 
 - less "novel" (relatively speaking, that is... as this datatype has barely even made it into widespread use yet!)

#### Option 3. Cell Hashing (RNA + protein + sample barcode)
paper (Stoeckius 2018): https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1603-1

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE108313
 - 2 cell lines

Pros:
 - because this is a methods-focused experiment, there are fewer uncertainties, and more densely sampled measurements -> great for tool development as the biological novelties/uncertainties have been minimized
Cons: 
 - less ADTs than the original CITEseq's ~13 ADTs, since it was more focused on optimizing titrations
 - less biologically interesting; more of a proof-of-concept paper to show that sample multiplexing is possible via oligo barcoding by sample

#### Option 4. ECCITE-seq (RNA + protein + sample barcode + VDJ clonality + CRISPR sgRNA)
paper (Mimitou 2019): https://www.biorxiv.org/content/10.1101/466466v1

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126310
 - ~49 ADTs

Pros:
 - most number of modalities


## Resources

### Computing

Most data analysis can be done on your own laptop (especially if you already have popular data science analysis software installed). Please bring a laptop (+ charger) if you're interested in participating. 

For some specific tasks that require heavy-lifting, access to [Rivanna](https://arcs.virginia.edu/rivanna), the large-scale computing cluster at UVA is useful. Most UVA affiliates can request access, if you do not already have it (see instructions on UVA ARCS website, as well as guides on how to use it, and an intro UNIX tutorial). 

Current T32 trainees on the BDSTG should already be members of the `bds_tg` group on Rivanna. We have an allocation of disk space on Rivanna at `/sfs/lustre/allocations/bds_tg` 
 - can optionally set an environment variable to point to this for easy communication: `export BDSDATA="/sfs/lustre/allocations/bds_tg"`
 - can also spend virtual compute credits using the shared compute allocation, also called `bds_tg` (use `allocations` command to see which ones you have access to)

Please commit any code into this repository (the repo you're reading right now). Start new folders for code, or other work. 


### Tools

The tools in this space are all relatively new, with more growing by the day. 

Feel free to look for others, reference any you find useful, and mix & match to make the most of analyzing/integrating data. There may be overlap between tools, especially if they are "tools of tools" built on the same underlying algorithms or popular base libraries. 

scRNAseq toolkits:
 - seurat (R), https://github.com/satijalab/seurat
 - scanpy (python), https://github.com/theislab/scanpy
 - scVI & scANVI (python), https://github.com/YosefLab/scVI
 - SCope (python), https://github.com/aertslab/SCope

Data Structures for large multi-feature + metadata handling:
 - hdf5-based "loom" -> https://linnarssonlab.org/loompy/format/index.html
  - https://github.com/linnarsson-lab/loompy
  - https://github.com/mojaveazure/loomR
 - https://github.com/theislab/anndata
 - https://github.com/pydata/xarray
 
## Tutorials

<to be filled>
 
