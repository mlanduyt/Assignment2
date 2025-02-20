from ihardening import *
from khardening import *


def test_sign ():
    x = 5
    y = det_sign(x)
    assert y == 1


def test_zero ():
    x = 0 
    y = det_sign(x)
    assert y == 0

def test_hardening ():
    E = 2
    Et = 1
    H = hardening (E,Et)
    assert H == 2 

def ktest_zeros ():
    E = 10
    Et = 2
    Y0 = 0
    sig_n = 0
    eps_n = 0
    alpha_n = 0
    del_eps = 0
    E = 0
    H = 0
    Y = 0
    sig_n, eps_n, alpha_n = kpredictor(sig_n, eps_n, alpha_n, del_eps, E, H, Y0)
    print (sig_n1, eps_n1, alpha_n1)
    x = sig_n+eps_n+alpha_n
    assert x == 0
    
def test_ipredictor ():
    E = 10
    Et = 2
    Y0 = 0
    sig_n = 0
    eps_n = 0
    del_eps = 0
    E = 0
    H = 0
    Y0, sig_n, eps_n = ipredictor (Y0, E, del_eps, sig_n, H, eps_n)
    x = Y0 +sig_n+eps_n
    assert x == 0