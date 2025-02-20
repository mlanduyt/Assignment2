from variables import list1

def sign (x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1

import random
list2 = list1
# define function, tol used to define tolerance

def bisection (f, a, b, tol):

    # a and b must be of opposite sign
    if sign(f(a)) == sign(f(b)):
        a = random.choice(list1)
        b = random.choice(list1)
        return bisection (f, a, b, tol)

    # establish midpoint 
    m = (1/2)*(a+b)

    if abs(f(m)) < tol:
        return m
        print (m)
    # midpoint meets satisfying condition

    elif sign(f(a)) == sign(f(m)):
        return bisection (f, m, b, tol)
        # midpoint replaces a

    elif sign(f(b)) == sign(f(m)):
        return bisection (f, a, m, tol)
        # midpoint replaces b

