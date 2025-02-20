### Summary
The main function of this code is executed by the running the 'tutorial' file. Example 5 allows for user input. 

This program is designed to execute material modeling using either the isotropic hardening or kinematic hardening.

Initial values used for calculation are all contained within the tutorial file, these may be changed as the user sees fit. 

These methods may be used as a valuable tool, but there are drawbacks in their assumptions which should be understood before using their results as truth. 

### Getting Started

All modules required should be self-contained and installed as part of the script.

### Testing

Pytest will run the testing script using predetermined variables with a known result to test the function's functionality. 
```bash
pytest
```


### File Details

ihardening contains the isotropic hardening method and functions

khardening contains the kinematic hardening method and functions

test_functions.py contains the test script, run by pytest

tutorial.ipynb contains multiple examples which may be run. Example 5 contains the case in which user import may be utilized. 
