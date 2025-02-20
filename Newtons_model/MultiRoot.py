#Import Info from other scripts
import random
from function2 import *
import os
from pathlib import Path

#Define Example function
f = lambda x: x**2 - 3
list1 = range (-50,50)

#Used to evaluate method 4 times, outputs second root if found
def multi_root(f):
    x0 = random.choice (list1)
    root1 = newtons_method (f, x0, tol)
    x3 = random.choice (list1)
    root2 = newtons_method (f,x3,tol)
    if root2-root1 < 2*tol:
        x0 = x0*-1
        root3 = newtons_method(f,x0,tol)
        return root3
    else:
        #print (root1) and (root2)
        roots = [root1, root2]
        return roots

