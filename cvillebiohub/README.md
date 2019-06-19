# CvilleBioHub Presentation

This presentation was given June 19, 2019 to a group of UVa graduate students and post-docs along with others in the Charlottesville community with an interest in biomedical data science. The event was co-sponsored by the [UVa Biomedical Data Sciences Training Program](http://bme.virginia.edu/bds/) and [CvilleBioHub](https://cvillebiohub.org/).

## How to view

### 1. Download
Options
* `wget https://github.com/databio/bdshack19/blob/master/cvillebiohub/hack2019-pres.tar.gz`
* `curl -O https://github.com/databio/bdshack19/blob/master/cvillebiohub/hack2019-pres.tar.gz`

### 2. Unpack
* `tar -xvzf hack2019-pres.tar.gz`

### 3. Open
Options
* `firefox hack2019-presentation/hackathon-2019-pres-final.html`
* `open -a Firefox hack2019-presentation/hackathon-2019-pres-final.html`

## How it was created

### 1. Create base file with [Markdown](https://daringfireball.net/projects/markdown/) in text editor of choice
* `hackathon-2019-pres-final.md`

### 2. Convert to [reveal.js](https://revealjs.com/#/) html presentation with [Pandoc](https://pandoc.org/) in shell
* `pandoc -t revealjs -s -o hackathon-2019-pres-final.html hackathon-2019-pres-final.md`

### 3. Package the html code with the assets
* `tar -zcvf hack2019-pres.tar.gz hack2019-presentation/`
