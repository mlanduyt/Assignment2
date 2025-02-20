from variables import *
from function1 import *

import os

def test_error ():
    f = lambda x: 2*(x+2)
    tol = 0.01
    a = -5
    b = 10
    # Call the bisection method
    root = bisection (f, a, b, tol)
    #Define Error, expected answer = -2
    error = root + 2
    assert tol>error

def test_input():
    f = lambda x: x
    tol = 0.01
    z = a+b
    assert z < 100.1

def test_sign():
    x = 5
    y = sign(x)
    assert y == 1
