# BDS Hackathon 2019

   * [BDS Hackathon 2019](#bds-hackathon-2019)
      * [1. About](#1-about)
         * [Skills required](#skills-required)
         * [Expectations](#expectations)
      * [2. Logistics](#2-logistics)
         * [Date/Time](#datetime)
         * [Location](#location)
         * [Live Chat: Slack + Twitter](#chat-and-social-media)
           * [2019 Organizers](#2019-organizers)
      * [3. Outline of the deliverable](#3-deliverable)
         * [Packaging structure](#packaging-structure)
         * [Parsing](#parsing)
         * [Python object](#python-object)
         * [Visualization](#visualization)
         * [Machine learning](#machine-learning)
      * [4. Data](#4-data)
         * [Option 1. pi-ATAC](#option-1-pi-atac-atac--protein)
         * [Option 2. sci-CAR](#option-2-sci-car-rna--atac)
         * [Option 3. CITE-seq](#option-3-cite-seq-rna--protein)
         * [Option 4. Cell Hashing](#option-4-cell-hashing-rna--protein--sample-barcode)
         * [Option 5. ECCITE-seq](#option-5-eccite-seq-rna--protein--sample-barcode--vdj-clonality--crispr-sgrna)
      * [5. Resources](#5-resources)
         * [Computing](#computing)
         * [Tools](#tools)
            * [General Purpose tools](#general-purpose-tools)
            * [scRNAseq toolkits](#scrnaseq-toolkits)
            * [Data Structures for large multi-feature & metadata handling](#data-structures-for-large-multi-feature--metadata-handling)
         * [Tutorials](#tutorials)


---
## 1. About

The __Biomedical Data Sciences Training Program__ ([bds_tg](http://bme.virginia.edu/bds/)) is organizing a 2nd annual hackathon for April 4-5, 2019. This will be a 48-hour event nucleated by the current trainees on the Biomedical Data Science NIH T32 training grant, and will be open to other interested participants. Food will be provided to those who have RSVP'd to fuel a collaborative and productive 48 hours. 

Last year, the [prior hackathon](https://github.com/databio/bds_hackathon) analyzed the CITEseq dataset (one of the first multi-omic single-cell datasets) and presented their efforts at the annual [UVA Datapalooza](https://www.youtube.com/watch?v=6qDEeRsMv7s&t=3808s). 

__This year__, we will apply collective skillsets of all attendees towards analyzing __single-cell resolution multi-omic data__, with the aim of producing a __python package__ that will automate aspects of analyzing this increasingly popular data type. 

#### Skills required
No previous skills are required to attend, but just one of any of the following could be helpful:
 - working knowledge of R or python in data wrangling or package development
 - some experience with statistical or machine learning libraries/packages
 - working knowledge of either cytometry or sequencing data types
 - working knowledge of mouse/human cell types and common biomarkers used for their identification or functional readout
 - experience with optimizing visualization and/or graphical design

Feel free to share this announcement with individuals you think might be interested in participating!

#### Expectations
 - have fun and make friends!
 - come with an appetite to learn, regardless of how advanced you may be in a particular area
 - embrace working together (you might temporarily go faster alone, but in the long run you'll only go farther as a team)
 - share your skills
   - teach others and be patient with those learning for the first time
   - the act of teaching forces you to synthesize your strategy and helps you (re)consider why you're doing something
 - ask questions (there are no stupid questions!)
   - in addition to what or how, ask each other WHY are you doing this? you may be surprised to find that it could lead to better ways of doing something, which may be especially clear when you're forced to remove the jargon and distill the main idea to a colleague



---
## 2. Logistics
 
### Date/Time
Thu Apr 4th 9am - Fri Apr 5th midnight

### Location
[Rice Hall](https://goo.gl/maps/TRenTumyx3P2) (computer science building)
 - if you have trouble getting in or finding your way, feel free to email organizers, or post in the slack channel (someone might be already there and can let you in)
 - __Room 128__, main room for both days (except Friday noon-2pm, we have to vacate temporarily)
   - light breakfast both days
   - dinner Thursday (Crozet Pizza)
   - dinner Friday (+dessert)!
 - __Room 242__, 
   - lunch Thursday: noon-2pm (Sticks Kebab)
 - Breakout groups feel free to spillover into lounge areas around Rice Hall, or elsewhere. 
   - __Room 514__, side room from 8-5 on Thursday.
   - __Room 204__, side room from 5PM Thursday to noon Friday and 5PM Friday until midnight.

### Presentation
After the dedicated 2-day hackathon concludes, we will aim to present the work to a broader audience (scheduling with [CvilleBioHub](https://cvillebiohub.org/) some time in ~May).

### Chat and Social Media

 - Slack: [`#hackathon2019` channel](https://uvacompbio.slack.com/messages/CHGLT0XMK/) in workspace `UVACompBio`. 
 - Twitter: UVa BDS [@uva_biodatasci](https://twitter.com/uva_biodatasci)

### 2019 Organizers
 - Nathan Sheffield (ns5bc), [website](http://databio.org/)
 - Gregory Medlock (glm5uh), prior bdstg trainee
 - Jeffrey Xing (jcx9dy), prior bdstg trainee

All three will be in and out throughout the event to help and respond to questions both in person and remotely.

Make sure to thank Jason and Kim for making this possible, and feeding you!
 - Jason Papin (jap8r)
 - Kimberly Fitzhugh-Higgins (kaf5r)

---
## 3. Deliverable

We seek to develop a python package to load, store, visualize, and analyze recently published single-cell multi-omic datasets (see data section below). We should take advantage of existing tools where available. Our python package will need to consider and implement these elements:

### Packaging structure
Making our functions installable and easily distributable would lead to convenient usage by others. Organizers can help here, when we get to this point!

Can take a look at cookie cutter examples/templates to guide initial development:
- could use as a template existing packages from group members: e.g. [medusa](https://github.com/gregmedlock/Medusa), [peppy](http://github.com/databio/peppy), [divvy](http://github.com/databio/divvy)
- [cookiecutter](https://github.com/audreyr/cookiecutter) helps with python package skeletons
- submit to pypi? conda?
- documentation? Could use [readthedocs](https://readthedocs.org/), [mkdocs](https://www.mkdocs.org/), or others?

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
## 4. Data

### Option 1. pi-ATAC (ATAC + protein)
paper (Chen 2018): https://www.nature.com/articles/s41467-018-07115-y
 - expands on scATACseq from (Buenrostro 2015): (https://www.nature.com/articles/nature14590)

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE112091
 - celltypes used: 
   - v6.5 mouse ESCs
   - human GM12878 lymphoblastoid cell line
   - human K562 CML cell line
   - mouse 4T1 breast tumor cell line
   - mouse splenocytes
   - mouse genetically engineered MMTV-PyMT breast tumor mouse model
 - validate celltype (de)mixing: mESC (n = 144) and human GM12878 (n = 144)
 - validate scATAC vs bulkATAC: GM17878 (n=168) vs 4 bulk replicates
 - validate protein indexing: GM12878 (n=298), indexed by CD19 and phospho-NFkB_p65_Ser536
 - protein abundance vs ATAC cell state: K562 nuclei (n=223), indexed by GATA2 TF (hi, med, low)
 - validate cell_line/normal (de)mixing: mouse 4T1 (n=95) & splenocyte (n=95), indexed by EpCAM and CD45
 - solid tumor/immune (de)mixing: MMTV-PyMT (n=369), indexed by EpCAM (n=177) and CD45 (n=192)
 - protein abundance vs tumor cell state: MMTV-PyMT (n=839), indexed by EpCAM+ and HIF1α
 - confirm hypoxia predicts cell state: 4T1 1%O2 at 6 timepoints, separate HIF1a staining + bulk-ATACseq

Pros: 
 - (relatively more) novel dataset with single-cell-resolution __epigenome__ modality (via ATAC)
 - methods-focused experiment (fewer biological uncertainties, and more densely sampled measurements) -> great for tool development as the biological novelties/uncertainties have been minimized

Cons: 
 - fewer total cells per sample (FACS sorting to 96-well plate)
 - least number of protein readouts (1-2 FACS antibodies)
 - less established tools -> more challenging to implement
 - data is less convenient -> spread across >2000 files (single well nature of data collection led to single file per cell)
   - ! unclear if protein signal is available (may need to contact authors)

### Option 2. sci-CAR (RNA + ATAC)
paper (Cao 2018): http://science.sciencemag.org/content/361/6409/1380

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE117089
 - HEK293T, human embryonic kidney cell line
 - NIH/3T3, mouse fibroblast cell line
 - A549, human lung adenocarcinoma–derived cells, after 0, 1, or 3 hours of 100 nM Dexamethasone treatment
 - cells from whole kidneys of two 8-week-old male mice
 
Pros: 
 - (relatively more) novel dataset with single-cell-resolution __epigenome__ and __transcriptome__ modalities (2 largest breadth)
 - data is neatly organized and pre-processed counts are available

Cons: 
 - modalities used are the largest 2 datatypes -> may be more unwieldy

associated scripts for processing sci-CAR
 - https://github.com/JunyueC/sci-CAR_analysis

### Option 3. CITE-seq (RNA + protein)
paper (Stoeckius 2017): https://www.nature.com/nmeth/journal/v14/n9/full/nmeth.4380.html

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100866
 - 13 cellular surface markers (via ADTs)

Pros:
 - same dataset analyzed in last year's hackathon; at some of the participants will already be familiar with the dataset -> potentially faster learning curve
 - data is neatly organized and pre-processed counts are available
 
Cons: 
 - less "novel" (relatively speaking, that is... as this datatype has barely even made it into widespread use yet!)

### Option 4. Cell Hashing (RNA + protein + sample barcode)
paper (Stoeckius 2018): https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1603-1

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE108313
 - cell lines: HEK293T, THP1, K562, and KG1
 - HEK293T (human) and NIH-3T3 (mouse)
 - human PBMC 

Pros:
 - methods-focused experiment (fewer biological uncertainties, and more densely sampled measurements) -> great for tool development as the biological novelties/uncertainties have been minimized
 - data is neatly organized and pre-processed counts are available

Cons: 
 - less ADTs than the original CITEseq's ~13 ADTs, since it was more focused on optimizing titrations
 - less biologically interesting; more of a proof-of-concept paper to show that sample multiplexing is possible via oligo barcoding by sample

included tool for decoding indexes from CITE-seq/Cell-hashing data: 
 - https://hoohm.github.io/CITE-seq-Count/Running-the-script/#antibody-barcodes-structure 
 - only necessary if working with raw sequence data; not needed if using processed counts data

### Option 5. ECCITE-seq (RNA + protein + sample barcode + VDJ clonality + CRISPR sgRNA)
paper (Mimitou 2019): https://www.biorxiv.org/content/10.1101/466466v1

Data from GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126310
 - ~49 ADTs representing surface protein markers

Pros:
 - most number of modalities, including novel modalities (VDJ) and CRISPR
 - _largest_ number of simultaneous protein markers (desired for cell phenotype readout)
 - data is neatly organized and pre-processed counts are available

Cons: 
 - more modalities to deal with (though could selectively ignore, or prioritize)


---
## 5. Resources

### Computing

Throughout the event, please __commit any code into this repository__ (the repo you're reading right now). Start new folders for code, or other work. And most importantly, remember to __document your work__ and thought process, as if a colleague were reading it for the first time.

Most data analysis can be done on your own laptop (especially if you already have popular data science analysis software installed). Please __bring a laptop (+ charger)__ if you're interested in participating!

For some specific tasks that require specialized environments and/or heavy-lifting, access to [Rivanna](https://arcs.virginia.edu/rivanna), the large-scale computing cluster at UVA is useful. UVA affiliates can request access, if you do not already have it (see instructions on UVA ARCS website, as well as guides on how to use it, and an intro UNIX tutorial). 
 - In addition to 50GB of permanent storage on `/home/computingid` (check with `hdquota`), 
 - each user also has 10TB of short/medium-term storage on `/scratch/computingid` (check with `sfsq`), 
   - which is plenty of space for the vast majority of your needs. 
 - Finally, there are existing versions of software libraries, enviornments, and even interactive notebook servers that are pre-configured on Rivanna, which you may find useful if you don't want to manage all of this yourself. 

Current T32 trainees on the BDSTG should already be members of the `bds_tg` group on Rivanna. Anybody in this group will already be able to access an additional allocation of permanent disk space on Rivanna at `/sfs/lustre/allocations/bds_tg` 
 - can optionally set an environment variable to point to this for easy communication: e.g. `export BDSDATA="/sfs/lustre/allocations/bds_tg"`
 - can also spend virtual compute "credits" (SU) using the shared compute allocation, also called `bds_tg` (use `allocations` command to see which ones you have access to)
 
We've recently just created a `bdshackathon` Rivanna group and added those who have RSVP'd to it. In theory, this should automatically grant access to rivanna, with a temporary number of credit hours allocated that should be sufficient to get started until you [request your own](https://arcs.virginia.edu/allocations). See: 
 - [login and file transfer](https://arcs.virginia.edu/login-and-file-transfer)
 - [rivanna interactive webportal](https://arcs.virginia.edu/ood)
   - for most work, we recommend logging into the web portal https://rivanna-portal.hpc.virginia.edu (netbadge required)
   - and starting an interactive jupyterlab or Rstudio server with 1 cpu/core (since most functions are single-threaded, and you don't want to waste credit hours)

Shared folder on Rivanna (for all hackathon attendees):
 - `/project/shefflab/bdshack19`  (accessible from the Rstudio or JupyterLab rivanna apps)
 - `/sfs/lustre/allocations/shefflab/bdshack19`


### Tools

The tools in multi-omic single-cell resolution analysis are all relatively new, with more growing by the day. 

Feel free to look for others, reference any you find useful, and mix & match to make the most of analyzing/integrating data. There may be overlap between tools, especially if they are "tools of tools" built on the same underlying algorithms or popular base libraries. 

Depending on your goal, it may be quicker to wrangle tabular data using existing general-purpose data science libraries that you're already familiar with. In other cases, it will be absolutely necessary to leverage existing tools, instead of re-inventing the wheel on a complicated function. We encourage you to work together, divide-and-conquer, and switch back-and-forth accordingly to make the most of time available. 

#### General Purpose tools
 - interactive data science environments
   - Rstudio, jupyter, zeppelin (first 2 are now available on Rivanna)
   - Excel or [Tableau](https://www.tableau.com/academic/students)
     - worth mentioning for those with little coding experience, but want to also get hands-on with data in a short time window
 - python
   - pandas (data wrangling)
   - scikit-learn (multi-purpose machine learning), or other specialized deep learning libraries
   - matplotlib, seaborn, bokeh, plotly (plotting)
 - R
   - dplyr from tidyverse (data wrangling)
   - [too many ML libraries to list](https://www.quora.com/What-are-the-best-machine-learning-packages-in-R)
     - [cluster analysis](http://www.sthda.com/english/wiki/factoextra-r-package-easy-multivariate-data-analyses-and-elegant-visualization)
   - ggplot2, plotly (plotting)
 - Software development and deployment
   - cookiecutter (https://cookiecutter.readthedocs.io/en/latest/readme.html), which implements a simple version of some of the items below
   - PyPI deployment (https://pypi.org/ e.g. enable "pip install" for our package)
   - Unit tests w/ pytest (https://docs.pytest.org/en/latest/)
   - Continuous integration (https://travis-ci.org/ - automatically runs tests and reports changes for every commit/pull request)

#### scRNAseq toolkits
 - seurat (R), https://github.com/satijalab/seurat
 - scanpy (python), https://github.com/theislab/scanpy
 - scVI & scANVI (python), https://github.com/YosefLab/scVI
 - SCope (python), https://github.com/aertslab/SCope
 - informal lists:
   - https://github.com/agitter/single-cell-pseudotime

#### Data Structures for large multi-feature + metadata handling
 - hdf5-based "loom" -> https://linnarssonlab.org/loompy/format/index.html
  - https://github.com/linnarsson-lab/loompy
  - https://github.com/mojaveazure/loomR
 - https://github.com/theislab/anndata
 - https://github.com/pydata/xarray

### Tutorials

Feel free to add here, if you find useful ones. 

