import random
tol = 0.001
#list1 = range (-50,50)

#f = lambda x: x**2 - 6

# define function, tol used to define tolerance
def newtons_method (f, x0, tol):
    #parameters to numerically guess derivative or 'slope'
    r = 0.05
    a = (x0+r)
    b = (x0-r)
    #'slope' or tangent found to initially guess root
    tangent = (f(a)-f(b))/(2*r)
    #attempt to resolve if the slope is found to be near zero
    if abs(tangent) < 0.2:
        x0 = x0+1
        return newtons_method (f, x0, tol)
    else:
        x1 = x0 - (f(x0)/tangent)
    y = f(x1)
    if y < tol:
        root = x1
        #print (root)
        return root
    elif y >= tol:
        x0=x1
        return newtons_method (f, x1, tol)

