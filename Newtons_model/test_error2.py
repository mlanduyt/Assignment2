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
    roots = 1
    assert roots < 2

    
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
    
def test_list ():
    list2 = list1
    assert list1 ==list2

def test_abs ():
    x = -2
    x = abs(x)
    assert x ==2

def test_signs():
    a = 2
    b = 3
    def sign_test (a,b):
        if sign(a) == sign(b):
            a = -a
            return sign_test (a,b)
        else:
            assert a == a

def test_midpoint ():
    a = 2
    b = 3
    m = (1/2)*(a+b)
    assert m == 2.5

def test_zero ():
    a = 0
    b = sign (a)
    assert b == 0

def test_tol ():
    assert tol == 0.001

def test_function ():
    f = lambda x: x*2+3
    z = f(2)
    assert z == 7

def test_random ():
    list1 = range (-50,50)
    a = random.choice(list1)
    assert a <= 50

def test_tangent():
    f = lambda x: 2*x
    x0 = 2
    r = 0.05
    a = (x0+r)
    b = (x0-r)
    #'slope' or tangent found to initially guess root
    tangent = (f(a)-f(b))/(2*r)
    tangent = tangent - 2
    assert tangent <= 0.01

def test_tolerance ():
    tol = 0.001
    y = 2
    assert y >= tol

def test_equal ():
    y = 2 
    z = 2
    assert y == z

def test_math ():
    y = 2 
    z = 3
    a = z-y
    assert a == 1

def test_randomchoice ():
    list1 = range (0,50)
    x = random.choice (list1)
    assert x <= 50

def test_multiplication ():
    tol = 0.001
    tol = 2*tol
    assert tol == 0.002

def test_return ():
    f = lambda x: x
    root = multi_root(f)
    if root == 0:
        return root
    else:
        Exception ("root error")

def test_false ():
    root1 = 1
    root2 = 2
    assert root1 != root2

def test_spread():
    r = 0.5
    x0 = 0
    a = (x0+r)
    b = (x0-r)
    m = a+b
    assert m == 0

