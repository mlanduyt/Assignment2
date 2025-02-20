from function2 import *
from MultiRoot import *
import os
from pathlib import Path
import random

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
    F = lambda x: x**2
    root = multi_root(f)
    root = root
    assert root < 2

    
def test_multi ():
    f = lambda x: 2*x + 3
    root = multi_root(f)
    assert root <= 10

def test_list ():
    list = list1
    assert all(list1) <= 51

def test_roots():
    f = lambda x: x
    roots = multi_root (f)
    assert roots < 0.001 
    



