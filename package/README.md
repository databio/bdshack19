# Packaging

Here are some initial attempts to package our deliverable. I start by manually creating what seem to be the minimum package requirements based on a quick tutorial I found [here](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html) and then test what a [cookiecutter](https://github.com/audreyr/cookiecutter-pypackage) package looks like. I would also like to explore the approach introduced in [peppy](https://github.com/pepkit/peppy), but I haven't done that yet.

## Manual creation

Since the [MadPy](https://pypi.org/project/Madpy/) name was taken on PyPI, I started with a working name of MoPy. I emailed thk@madpy.org, but I do not expect to get a response as the repository hasn't been touched in over a decade. [PEP 541](https://www.python.org/dev/peps/pep-0541/) details the process for resolving name disputes, in particular in the setting of [abandoned projects](https://www.python.org/dev/peps/pep-0541/#removal-of-an-abandoned-project), but I have not gotten far in this process.

I start with creation of a `/MoPy` parent directory within this one, add empty `/bin` and `/docs` directories, and then copy a development version of the `multianndata.py` base script into a `/mopy` directory. I include `CHANGES.md`, `LICENSE.md`, and `README.md` files and start to describe an overview of the project in the `README.md` file. I use the BSD-2 license as the license. I then write the `setup.py` script for creating the distribution, run it with `python setup.py sdist`, which generates the `/dist` directory with the distribution in a tarball.

I tried unsuccessfully to register and upload the distribution to PyPI. I will try again later.

## cookiecutter creation

As an alternative to manual package creation, I make the `/cookie` directory and try the `cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git` command. This generates a lot of files that overwhelms me, and since I have a surgery meeting to attend, I put the project on indefinite hold.
