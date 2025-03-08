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
pip install -e .
```
### Background
This code is meant to create and solve strutural response. This is performed by defining nodes, connecting them through matrices, assigning boundary conditions and external forces. This code determines displacements, rotations, and internal forces; which are subsequently utilized to determine the buckling mode and shape. 

### Examples/Template
The problems required to be solved are worked out under the example folder, a template is provided to be filled out for any future problem. 

### Tests
Tests are executed via the Pytest function

