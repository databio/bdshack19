Instructions for installation and package management will go here, with emphasis on getting things up and running on Rivanna.

## Python environments on Rivanna

Rivanna lets users use Anaconda for environment management. Best practice is to create an environment for each project you are working on; for example, you might want to create a separate anaconda environment for this hackathon.

When you create an environment, any package you install will only be installed within that environment. You can also control the version of python used within the environment. Each environment you create should also be accessible as an independent kernel in jupyterlab.

First, load anaconda when you've connected to Rivanna.

```
module load anaconda
```

Then create an environment:

```
conda create --name bdshack2019
```

To enter the environment, type:

```
source activate bdshack2019
```

if you'd like to leave the environment, type:

```
source deactivate
```

While you're in the environment, installing packages is done like below. We'll use the scanpy package as an example, which has requirements installed via conda, and then is itself installed with pip (another package manager):

```
conda install seaborn scikit-learn statsmodels numba
conda install -c conda-forge python-igraph louvain
pip install -U scanpy
```

In order to get this environment to show up as a kernel in jupyterlab, you'll have to manually activate an ipython kernel for the environment. Run the following while you're in the environment:

```
python -m ipykernel install --user --name bdshack2019 --display-name "Python (bdshack2019)"
```

After running this command, reboot your jupyterlab instance and the kernel should appear as an option in the tile view when creating a new notebook.
