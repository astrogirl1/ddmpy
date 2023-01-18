from distutils.sysconfig import get_config_var
import matplotlib.pyplot as plt
import numpy as np

mass_bino = 100 
# pe = np.linspace(1e-11, 1e-2, num=100)
tau = np.linspace(1e+6, 1e+26, num=100)

def func(tau_result):
    delta_m = 1/(tau_result/(2.3e+7))**(1/3)
    fdm_result = delta_m/mass_bino
    return fdm_result

fdm = np.ones(len(tau))
for idx, val in enumerate(tau):
    fdm[idx] = func(val)

plt.loglog(tau, fdm)
plt.show()