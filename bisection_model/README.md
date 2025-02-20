### Summary

This code may be cloned via git clone https://github.com/mlanduyt/Bisection_Method/

The main function of this code is executed by the running the 'run' file.

This program is designed to execute the bisection method to determine the root of any continuous function. 

This is accomplished by defining variables under the variables.py file. This will allow for the changing of the function being evaluated 'f' and the tolerance 'tol'. 

Two random values; 'a' and 'b' are selected randomly, bounded by 'list1' in variables, 'a' and 'b' are randomly reselected should they not encapsulate a root. The range of this list can be changed under the bisection function found in function.py. 

### Getting Started

### Conda environment, install, and testing <a name="install"></a>

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name bisection-method-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate bisection-method-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
### Testing

Pytest will run the testing script using predetermined variables with a known result to test the function's functionality. 
```bash
pytest
```


### File Details

function.py contains the bisection method function called and executed by both the run and test scripts

variables.py defines the variables used to run the bisection method. This is where the function (such as f = 2x) being evaluated my be changed

test_error.py contains the test script, run by pytest

Run executes the files listed above. 