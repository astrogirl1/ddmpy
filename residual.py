import matplotlib.pyplot as plt
import numpy as np
import itertools

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output23/lcdm_hyrec_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-50_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-25_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-10_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-5_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-3_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-2_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps5e-2_cl.dat']

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_lcdm_cl.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+19_pe1e-2_fdm1e-4_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+22_pe1e-3_fdm1e-5_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+25_pe1e-4_fdm1e-6_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+31_pe1e-6_fdm1e-8_cl.dat"]

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_lcdm_cl.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+13_pe1e-6_fdm1e-9_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+14_pe1e-6_fdm1e-9_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+16_pe1e-6_fdm1e-9_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/exotemp/exo_tau2e+18_pe1e-6_fdm1e-9_cl.dat"]

# Gamfiles = ['/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_lcdm_cl.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g800eps0.1_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g300_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.1_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g10eps0.1_cl.dat"]

# Pkfiles = ['/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_lcdm_z2_pk.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.001_z1_pk.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.01_z1_pk.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.1_z1_pk.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.5_z1_pk.dat"]

# PkGamfiles = ['/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_lcdm_z1_pk.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g300_z1_pk.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g100_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.1_z1_pk.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g10eps0.1_z1_pk.dat"]

#files = ['/Users/dipan/class_decays-merging_with_master/output/lcdm_poulincl.dat',"/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv300_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv100_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv60_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv30_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv15_cl.dat"]

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/january/lcdm_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.001_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.01_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.1_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.5_cl.dat']

data = []

for data_file in files:
    data.append(np.loadtxt(data_file))
# roots = ['lcdm_hyrec_cl', 'test_g3.75', 'test_g1_cl', 'test_g0.1',
# 'test_g0.02', 'test_g0.0002', 'test_g0.000002', "test_g0.000002_eps1e-50"]
#roots = ['lcdm', "g^-1 = 300","g^-1=100","g^-1=60","g^-1=30","g^-1=15"]
# # roots = [r'$\Lambda$ CDM - no decay', r'$\tau$= $10^{13}$ s', r'$\tau$= $10^{14}$ s', r'$\tau$= $10^{16}$ s', r'$\tau$= $10^{18}$ s']
# roots = [r'$\Lambda$ CDM-no decay', r'$E_{\gamma}$= $10^{-4}$ GeV', r'$E_{\gamma}$= $10^{-5}$ GeV', r'$E_{\gamma}$= $10^{-6}$ GeV', r'$E_{\gamma}$= $10^{-7}$ GeV']

# roots = [r'$\Lambda$CDM', r'$\tau_{dec}=10^{19}$ s', r'$\tau_{dec}=10^{22}$ s', r'$\tau_{dec}=10^{25}$ s', r'$\tau_{dec}=10^{31}$ s']

roots = [r'$\Lambda$CDM', r'$E_{\gamma}=10^{-2}$GeV, $\tau=10^{19}$s ', r'$E_{\gamma}=10^{-3}$GeV, $\tau=10^{22}$s',r'$E_{\gamma}=10^{-4}$GeV, $\tau=10^{25}$s', r'$E_{\gamma}=10^{-6}$GeV, $\tau=10^{31}$s']

# roots = [r'$\Lambda$CDM', r'$\epsilon$ = 0.005 ', r'$\epsilon$ = 0.009 ', r'$\epsilon$ = 0.01']
#color = ['black', 'goldenrod','orange', 'darkorange', 'red', 'blueviolet'] 

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
#TT#
index0, curve0 = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'k'
ylim = []
xlim = []
# x = []
# y = []
# x.append(curve0[:, 0])
# y.append(curve0[:, 1])
# print(y)
ax1.semilogx(curve0[:, 0],(curve0[:, 1]), color='black', linewidth=1.5, linestyle='dashdot')
ax2.semilogx(curve0[:, 0],(curve0[:, 1]), color='black', linewidth=1.5, linestyle='dashdot')

index, curve = 1, data[1]
ax1.semilogx(curve[:, 0], (curve[:, 1]),linestyle='dashed',color='blue')
ax2.semilogx(curve[:, 0], (curve[:, 1])/(curve0[:, 1])-1,linestyle='dashed',color='blue')

index, curve = 2, data[2] 
ax1.semilogx(curve[:, 0], (curve[:, 1]),linestyle='dashed',color='tab:green')
ax2.semilogx(curve[:, 0], (curve[:, 1])/(curve0[:, 1])-1,linestyle='dashed',color='tab:green')

index, curve = 3, data[3] 
ax1.semilogx(curve[:, 0], (curve[:, 1]), linestyle='dashed',color='orange')
ax2.semilogx(curve[:, 0], (curve[:, 1])/(curve0[:, 1])-1,linestyle='dashed',color='orange')

index, curve = 4, data[4] 
ax1.semilogx(curve[:, 0], (curve[:, 1]), linestyle='dashed',color='red')
ax2.semilogx(curve[:, 0], (curve[:, 1])/(curve0[:, 1])-1, linestyle='dashed', color='red')


ax1.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='upper left', fontsize=17)

ax2.set_xlabel('$\ell$', fontsize=20)
ax1.set_ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=20)
ax2.set_ylabel(r'$\frac{C_\ell^{\mathrm{TT}}(\Lambda DDM)}{C_\ell^{\mathrm{TT}}(\Lambda CDM)}-1$',fontsize=20)

plt.subplots_adjust(wspace=0,hspace=0)
plt.xticks(fontsize=20)
ax1.tick_params(labelsize=18)
ax2.tick_params(labelsize=18)
plt.savefig("chap4gam.pdf", format="pdf")
plt.show()


