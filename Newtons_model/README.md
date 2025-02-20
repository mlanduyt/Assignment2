### Summary

This code may be cloned via git clone https://github.com/mlanduyt/Newtons_Method/

The main function of this code is executed by the running the 'tutorial' file.

This program is designed to execute newton's method to determine the root of any continuous function. This uses the derivative of a function to 'guess' the root, finding the local value and repeating until the value of the function is within a tolerance range of the zero.

The initial value; 'x0' is selected randomly, bounded by 'list1' in variables. In an attempt to test for multiple roots, such as for a binomial function, multiple guesses are made and multiple results are reported. 

Newton's method is a valuable tool for evaluating roots, but may find issues with derivatives near zero, as their 'guess' may not zero in on the solution. This method also does not inherently provide errors associated with non-convergence. 

### Getting Started

All modules required should be self-contained and installed as part of the script.

### Testing

Pytest will run the testing script using predetermined variables with a known result to test the function's functionality. 
```bash
pytest
```


### File Details

function.py contains newton's method function called and executed by both the run and test scripts. This script contains tolerance 'tol' which may be changed to affect accuracy.

MultiRoot.py runs the script multiple times in order to test for multiple roots.

test_error.py contains the test script, run by pytest

tutorial.ipynb contains multiple examples which may be run
