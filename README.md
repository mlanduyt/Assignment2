### Getting Started

### Conda environment, install, and testing <a name="install"></a>

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name XXX-method-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate XXX-method-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
install the applicable pips utilized for this code
```bash
pip install numpy
pip install pathlib
```

This code is meant to create and solve structural matrices, these can be defined by creating node points which are then connected via 'connections'. The inputs for this analysis can be found in the tutorial.ipynb section of this file. These numbers may be changed and evaluated by the solver which calls the main portion of the analysis from analysis.py. Some functions are utilized from the math_utils.py script.