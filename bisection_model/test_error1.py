from variables import *
from pathlib import Path
from function1 import bisection
from function1 import sign
import random

def test_error ():
    f = lambda x: 2*(x+2)
    tol = 0.01
    a = -5
    b = 10
    # Call the bisection method
    root = bisection(f, a, b, tol)
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

def test_equal ():
    f = lambda x: 2*(x+2)
    tol = 0.01
    a = -5
    b = -5
    # Call the bisection method
    root = bisection(f, a, b, tol)
    #Define Error, expected answer = -2
    error = root + 2
    assert tol>error

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

def test_function ():
    f = lambda x: x*2+3
    z = f(2)
    assert z == 7

def test_random ():
    list1 = range (-50,50)
    a = random.choice(list1)
    assert a <= 50

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

def test_errors ():
    f = lambda x: 2**x-10
    tol = 0.01
    a = -5
    b = 10
    # Call the bisection method
    root = bisection(f, a, b, tol)
    #Define Error, expected answer = 3.3
    root = root-3.3
    assert root <= 3*tol