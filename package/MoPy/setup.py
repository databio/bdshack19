from distutils.core import setup

setup(
    name='MoPy',
    version='0.1.0',
    author='BDSHack2019',
    author_email='glm5uh@virginia.edu',
    packages=['mopy', 'mopy.test'],
    scripts=['mopy/multianndata.py'],
    url='http://pypi.python.org/pypi/MoPy/',
    license='LICENSE.txt',
    description='A multi-omics ready data class.',
    long_description=open('README.txt').read(),
    install_requires=[
        "logging >= 0.4.9.6",
        "pandas >= 0.24.2",
        "pybedtools >= 0.8.0",
        "scanpy >= 1.4",
        "scipy >= 1.2.1",
    ],
)

### Notes

# We use semantic versioning as described by Tom Preston-Werner [here](https://semver.org/).
