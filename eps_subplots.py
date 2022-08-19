from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
import numpy as np
import itertools


# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam0.9_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.15_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.3_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.45_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.6_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.75_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.9_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.93_eps0.0067_cl.dat']

files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.001_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.003_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.005_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.007_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.009_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.01_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.015_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.02_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.025_cl.dat']

files2 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.001_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.003_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.005_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.007_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.009_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.01_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.015_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.02_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.025_cl.dat']

data1 = []
data2 = []
for data_file in files1:
    data1.append(np.loadtxt(data_file))

for data_file in files2:
    data2.append(np.loadtxt(data_file))


# roots = ['lcdm', '$\Gamma_{exo}$=1e-1', '$\Gamma_{exo}$=1e-3',
# '$\Gamma_{exo}$=1e-4', '$\Gamma_{exo}$=1e-7'] #km/s/Mpc
#roots = ['lcdm', 'tau = 3e9', 'tau = 1e10', 'tau = 3e10', 'tau = 1e11'] #Gyr
# roots = ['Planck2018',
# '$\Gamma^{-1}$ = 123.8 ',
# '$\Gamma^{-1}$ = 78.01 ',
# '$\Gamma^{-1}$ = 55.27 ', 
# '$\Gamma^{-1}$ = 49.26 ',
# '$\Gamma^{-1}$ = 34 ',
# '$\Gamma^{-1}$ = 24.64 ',
# '$\Gamma^{-1}$ = 17.48 ',
# '$\Gamma^{-1}$ = 12.38 ',
# '$\Gamma^{-1}$ = 11.54 ']  #Gyr

# roots = ['Planck2018',
# '$\epsilon$ = 0.001 ',
# # '$\epsilon$ = 0.005 ',
# '$\epsilon$ = 0.0067 ', 
# '$\epsilon$ = 0.01',
# '$\epsilon$ = 0.015 ',]
# # '$\epsilon$ = 0.02 ',
# # '$\epsilon$ = 0.025 ']
# # '$\epsilon$ = 12.38 ',
# # '$\epsilon$ = 11.54 ']  

roots = ['Planck2018',
'$\epsilon$ = 0.001 ',
'$\epsilon$ = 0.003 ',
'$\epsilon$ = 0.005 ', 
'$\epsilon$ = 0.007 ',
'$\epsilon$ = 0.009 ',
'$\epsilon$ = 0.01  ',
'$\epsilon$ = 0.015  ',
'$\epsilon$ = 0.02  ',
'$\epsilon$ = 0.025 ']  

# eps = [0, 0.001, 0.0067, 0.01, 0.015]
eps = [0, 0.001, 0.003, 0.005, 0.007, 0.009, 0.01, 0.015, 0.02, 0.025]
# fig, ax = plt.subplots()

fig, ax = plt.subplots(2, sharex=True, sharey=True, gridspec_kw={'height_ratios': [2, 3]})


y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

color = ['goldenrod','blue', 'green','chocolate', 'orangered', 'orchid', 'orange', 'magenta','red']

# color = ['black', 'goldenrod','orange', 'darkorange', 'red', 'blueviolet']

index0, curve0 = 0, data1[0]
index1, curve1 = 0, data2[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

# ax[1].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2)

n = len(data1[1:])
colors = plt.cm.cool_r(np.linspace(0, 1, n))
colors_l = cm.cool_r

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
       
    for i in range(n):
        ax[0].semilogx(curve[:, 0], (curve[:, 1]), color = colors[idx] , linewidth=1.3)

ax[0].set_title("$\epsilon$ varied, $\Gamma_{wdm}$ constant ", loc='center')
plt.ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=15)

for idx, dat in enumerate(data2[1:]):
    index, curve = idx, dat
       
    for i in range(n):
        ax[1].semilogx(curve[:, 0], (curve[:, 1]), color = colors[idx] , linewidth=1.3)

# fig.legend([root for (root, elem) in
#     itertools.product(roots, y_axis)], loc='best')

ax[1].set_xlabel('$\ell$', fontsize=16)
ax[1].set_xlim(3,2700)
ax[0].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2)
ax[1].semilogx(curve1[:, 0], (curve1[:, 1]), color='black', linewidth = 2.2)
ax[0].annotate(r'$\Gamma_{wdm}^{-1} = 55 Gyr$', xy=(10.5, 8e-10))
ax[1].annotate(r'$\Gamma_{wdm}^{-1} = 30 Gyr$', xy=(10.5, 8e-10))

# plt.ylabel(r'$\frac{C_\ell^\mathrm{TT}(\Lambda\mathrm{DDM})}{C_\ell^\mathrm{TT}(\Lambda \mathrm{LCDM})}-1$',fontsize=15)
plt.ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=15)
# plt.title("pe varied, $\Gamma_{exo}$ = 1e-2 km/s/Mpc ", loc='center')
normalize = mcolors.Normalize(vmin=min(eps), vmax=max(eps))
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colors_l)
scalarmappaple.set_array(eps)
# plt.colorbar(scalarmappaple)
fig.colorbar(scalarmappaple, orientation='horizontal', label='$\\epsilon$')
# plt.savefig('wdm_eps_1208',dpi=300)
plt.show()
plt.clf()

