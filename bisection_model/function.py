from variables import list1

import random
list2 = list1
# define function, tol used to define tolerance
def bisection(f, a, b, tol):

    # a and b must be of opposite sign
    if np.sign(f(a)) == np.sign(f(b)):
        a = random.choice(list1)
        b = random.choice(list1)
        return bisection (f, a, b, tol)

    # establish midpoint 
    m = (1/2)*(a+b)

    if np.abs(f(m)) < tol:
        return m
        print (m)
    # midpoint meets satisfying condition

    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection (f, m, b, tol)
        # midpoint replaces a

    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection (f, a, m, tol)
        # midpoint replaces b

