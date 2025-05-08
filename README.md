
[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)

[![codecov](https://codecov.io/gh/mlanduyt/Final_Project/graph/badge.svg?token=V8BG4FHMD7)](https://codecov.io/gh/mlanduyt/Final_Project)
[![tests](https://github.com/mlanduyt/Final_Project/actions/workflows/tests.yml/badge.svg)](https://github.com/mlanduyt/Final_Project/actions)


### Getting Started

### Conda environment, install, and testing <a name="install"></a>

To install this package, please begin by setting up a conda environment:
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
This code is designed to operate as a simple computational fluid dynamics solver. This simple solver uses the differential form of the navier stokes equation to step through fluid dynamics and solve for the expected flow response. The solver is used to calculate poiseuille and couette flow; and compared to expected analytical results. 

### Examples/Template
The tutorials provided evaluate fundamental pipe flow equations. The applicable navier stokes equations are described in each tutorial. 

## Poiseuille Flow
This flow in a pipe is driven by a pressure difference between each ends. Each wall provides a no-slip boundary condition, generating a flow as seen below: 

![alt text](poiseuille_flow.png)

## Couette Flow
This flow in a 'pipe' represents an analogy to a simple boundary layer, in which the bulk flow is simplified to a moving wall. This flow is evaluated as if a pipe existed with a no-slip motionless wall and a no-slip moving wall at some velocity. This flow is seen below:

![alt text](couette_flow.png)

### Tests
Tests are executed via the Pytest function. Code coverage is provided. 

