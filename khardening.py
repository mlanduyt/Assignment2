#this function, given a known strain, will provide stress using the kinematic hardening method
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

def kpredictor(sig_n, eps_n, alpha_n, del_eps, E, H, Y0):
    sig_trial = sig_n + E*del_eps
    alpha_trial = alpha_n
    eta_trial = sig_trial - alpha_trial
    psi_trial = abs(eta_trial)-Y0
    if psi_trial <= 0: #Elastic Deformation
        sig_n = sig_trial
        alpha_n = alpha_trial
        eps_n = eps_n
        return [sig_n, alpha_n, eps_n]
    else: #Plastic Deformation
        del_eps = (psi_trial)/(E+H)
        x = eta_trial
        sign = det_sign(x)
        sig_n = sig_trial - sign*E*del_eps
        alpha_n = alpha_n + sign*H*del_eps
        eps_n = eps_n + del_eps
        return [sig_n, alpha_n, eps_n]

