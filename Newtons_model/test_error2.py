from function2 import *
from MultiRoot import *
import os
from pathlib import Path

def test_error ():
    f = lambda x: 2*(x+2)
    tol = 0.01
    x0 = 0
    root = newtons_method (f, x0, tol)
    #Define Error, expected answer = -2
    error = root + 2
    if tol > error:
        print ("test passed")
    else:
        print ("test failed")

def test_zero():
    F = lambda x: -x**2
    root = multi_root(f)
    if all(root) < 1:
        print ("test passed")
    else:
        print ("test failed")
    

    
    



