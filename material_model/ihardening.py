#this function, given a known strain, will provide stress using the isotropic hardening method
# eps = strain
# sig = stress
# E = youngs (elastic) modulus
# Et = plastic modulus

#used for code testing
#E = 1000
#Et = 100
#Y0 = 10
#eps_n = 0
#sig_n = 0
#del_eps = 7.5

#Utilized internal function to not require numpy import
def det_sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0: 
        return -1 

# Defined hardening using tangent and youngs modulus
def hardening(E, Et):
    H = (E*Et)/(E-Et)
    return H


def ipredictor(Y0, E, del_eps, sig_n, H, eps_n):
    Yn = Y0+H*eps_n
    del_sig_trial = E*del_eps
    sig_trial = sig_n  + del_sig_trial
    #print ('sig_trial', sig_trial)
    psi_trial = abs(sig_trial) - Yn
    if psi_trial <= 0: #material is elastic
        sig_n = sig_trial
        eps_n = eps_n
        Y0 = Yn
        #print ('sig_n', sig_n)
        #print ('eps_n', eps_n)
        return [Y0, sig_n, eps_n]

    else: #material is yielding
        del_eps_n = psi_trial/(E+H)
        x = sig_trial
        sign = det_sign(x)
        sig_n = sig_trial - (sign*E*del_eps_n)
        eps_n = eps_n + del_eps_n
        #print ('sig_n', sig_n)
        #print ('eps_n', eps_n)
        return [Y0, sig_n, eps_n]


#print (sig_n1)
#print (eps_n1)


 
