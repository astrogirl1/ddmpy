from doctest import OutputChecker
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import itertools


files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output19/lcdm_hyrec_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.001_hyrec_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.01_hyrec_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.1_hyrec_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.5_hyrec_cl.dat']


files2 = ['/home/a1705053/Desktop/1908/class_decays/output/eps0_hyrec_cl.dat',
# '/home/a1705053/Desktop/1908/class_decays/output/eps0.001_hyrec_cl.dat',
# '/home/a1705053/Desktop/1908/class_decays/output/eps0.01_hyrec_cl.dat',
'/home/a1705053/Desktop/1908/class_decays/output/eps0.1_hyrec_cl.dat',
'/home/a1705053/Desktop/1908/class_decays/output/eps0.5_hyrec_cl.dat']

# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/january/lcdm_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.001_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.01_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.1_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.5_cl.dat']



data1 = []
data2 = []
for data_file in files:
    data1.append(np.loadtxt(data_file))

# for data_file in files2:
#     data2.append(np.loadtxt(data_file))


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

roots = ['Planck2018',
'$\epsilon$ = 0.001 ',
'$\epsilon$ = 0.01 ',
'$\epsilon$ = 0.1 ', 
'$\epsilon$ = 0.5 ']

eps = [0, 0.1, 0.5]
# eps = [0, 0.001, 0.003, 0.005, 0.007, 0.009, 0.01, 0.015, 0.02, 0.025]
# fig, ax = plt.subplots()

fig, ax = plt.subplots(3, sharex=True, sharey=True, gridspec_kw={'height_ratios': [2, 2, 2]})

y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

color = ['goldenrod','blue', 'green','chocolate', 'orangered', 'orchid', 'orange', 'magenta','red']
# color = ['dodgerblue','limegreen', 'red']
cmap1 = LinearSegmentedColormap.from_list("mycmap", color)

# color = ['black', 'goldenrod','orange', 'darkorange', 'red', 'blueviolet']

index0, curve0 = 0, data1[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

n = len(data1[1:])
colors = cmap1(np.linspace(0, 1, n))
colors_l = cmap1

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
       
    for i in range(n):
        ax[0].semilogx(curve[:, 0], ((curve[:, 1]/curve0[:, 1])-1), color = colors[idx] , linewidth=1.3)

ax[0].set_title("$\epsilon$ varied, $\Gamma_{wdm}$ constant ", loc='center')
ax[0].set_ylabel(r'$\frac{C_\ell^{\mathrm{TT}}(\Lambda DDM)}{C_\ell^{\mathrm{TT}}(\Lambda CDM)}-1$',fontsize=15)

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
       
    for i in range(n):
        ax[1].semilogx(curve[:, 0], ((curve[:, 2]/curve0[:, 2])-1), color = colors[idx] , linewidth=1.3)

ax[1].set_ylabel(r'$\frac{C_\ell^{\mathrm{EE}}(\Lambda DDM)}{C_\ell{^\mathrm{EE}}(\Lambda CDM)}-1$',fontsize=15)

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
       
    for i in range(n):
        ax[2].semilogx(curve[:, 0], ((curve[:, 5]/curve0[:, 5])-1), color = colors[idx] , linewidth=1.3)

ax[2].set_ylabel(r'$\frac{C_\ell^{\mathrm{\phi\phi}}(\Lambda DDM)}{C_\ell^{\mathrm{\phi\phi}}(\Lambda CDM)}-1$',fontsize=15)


ax[1].set_xlabel('$\ell$', fontsize=16)
ax[1].set_xlim(3,2700)
ax[0].set_ylim(-0.75, 0.75)
ax[1].set_ylim(-0.75, 0.75)
ax[2].set_ylim(-0.75, 0.75)
ax[0].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2, linestyle='dashed')
ax[1].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2, linestyle='dashed')
ax[2].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2, linestyle='dashed')


# plt.title("pe varied, $\Gamma_{exo}$ = 1e-2 km/s/Mpc ", loc='center')
normalize = mcolors.Normalize(vmin=min(eps), vmax=max(eps))
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colors_l)
scalarmappaple.set_array(eps)
# plt.colorbar(scalarmappaple)
fig.colorbar(scalarmappaple, orientation='horizontal', label='$\\epsilon$')
# plt.savefig('wdm_eps_1208',dpi=300)

# fig.legend([root for (root, elem) in
#     itertools.product(roots, y_axis)], loc='best')
fig.legend()

plt.show()
plt.clf()

