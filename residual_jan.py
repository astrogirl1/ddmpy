import matplotlib.pyplot as plt
import numpy as np
import itertools

## NOT USED####
# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output23/lcdm_hyrec_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-50_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-25_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-10_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-5_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-3_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-2_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps5e-2_cl.dat']

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output23/lcdm_hyrec_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-3_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps9e-2_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps8e-2_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps5e-2_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output23/test_g80_eps1e-2_cl.dat']

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/1909/hyrec_lcdm_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/1909/recfast_lcdm_cl.dat']

#files = ['/Users/dipan/class_decays-merging_with_master/output/lcdm_poulincl.dat',"/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv300_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv100_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv60_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv30_cl.dat","/Users/dipan/class_decays-merging_with_master/output/dcdm_gaminv15_cl.dat"]

### USED FOR REPRODUCING POULIN PAPER########

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_lcdm_cl.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g300_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g100_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.1_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g10eps0.1_cl.dat"]

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_lcdm_cl.dat',"/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.001_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.01_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.1_cl.dat", "/home/a1705053/Desktop/merged/merged_codes_may22/tempout/test_g30eps0.5_cl.dat"]

data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
# roots = ['lcdm_hyrec_cl', 'test_g3.75', 'test_g1_cl', 'test_g0.1',
# 'test_g0.02', 'test_g0.0002', 'test_g0.000002', "test_g0.000002_eps1e-50"]
#roots = ['lcdm', "g^-1 = 300","g^-1=100","g^-1=60","g^-1=30","g^-1=15"]
#roots = ['lcdm', 'g^-1 = 300','g^-1=100','g^-1=60','g^-1=30','g^-1=15']
roots = ['lcdm', r'$\Gamma_{wdm}^{-1}$ = 300 Gyr', '$\Gamma_{wdm}^{-1}$ = 100 Gyr', '$\Gamma_{wdm}^{-1}$ = 30 Gyr', '$\Gamma_{wdm}^{-1}$ = 10 Gyr']
# roots = ['Hyrec', 'Recfast']
# roots = [r'$\Lambda$CDM', r'$\epsilon$ = 0.001 ', r'$\epsilon$ = 0.01 ', r'$\epsilon$ = 0.1 ', r'$\epsilon$ = 0.5 ']

#color = ['black', 'goldenrod','orange', 'darkorange', 'red', 'blueviolet'] 

fig, ax = plt.subplots()
#TT#
index0, curve0 = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
# x = []
# y = []
# x.append(curve0[:, 0])
# y.append(curve0[:, 1])
# print(y)
ax.semilogx(curve0[:, 0],(curve0[:, 1]), color='black', linewidth=1.2)

index, curve = 1, data[1]
ax.semilogx(curve0[:, 0], (curve[:, 1]/curve0[:, 1])-1, color='tab:red')

index, curve = 2, data[2] 
ax.semilogx(curve[:, 0], (curve[:, 1]/curve0[:, 1])-1, color='tab:blue')

index, curve = 3, data[3] 
ax.semilogx(curve[:, 0], (curve[:, 1]/curve0[:, 1])-1, color='green')

index, curve = 4, data[4] 
ax.semilogx(curve[:, 0], (curve[:, 1]/curve0[:, 1])-1, color='goldenrod')


# index, curve = 5, data[5]  
# y_axis = [u'EE']  
# tex_names = ['TT']  
# x_axis = 'l'
# ylim = []  
# xlim = []  
# ax.semilogx(curve[:, 0], (curve[:, 1])/(curve0[:, 1])-1)
# ax.plot(curve[:, 0], (curve[:, 1]/curve0[:, 1])-1)

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='lower left', fontsize=18)

ax.set_xlabel('$\ell$', fontsize=20)
ax.tick_params(labelsize=18)

ax.set_ylabel(r'$\frac{C_\ell^{\mathrm{TT}}(\Lambda DDM)}{C_\ell^{\mathrm{TT}}(\Lambda CDM)}-1$',fontsize=22)
# ax.set_title(r"Residual plot with $\epsilon$ varied, $\Gamma_{wdm}^{-1}$= 30 Gyr ", loc='center')
# ax.set_title(r"Residual plot for Hyrec vs Recfast", loc='center')
ax.set(xlim=(2.5, 2700), ylim=(-0.17, 0.17))
plt.show()


