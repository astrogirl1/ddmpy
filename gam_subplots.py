from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import itertools

files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.3_eps0.0067_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.45_eps0.0067_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.6_eps0.0067_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.75_eps0.0067_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.9_eps0.0067_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.93_eps0.0067_cl.dat',]

# files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo1e+20_wdm1.25_pe10_eps0.007_mass100_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo5e+20_wdm1.25_pe10_eps0.007_mass100_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo5e+21_wdm1.25_pe10_eps0.007_mass100_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo5e+22_wdm1.25_pe10_eps0.007_mass100_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo5e+23_wdm1.25_pe10_eps0.007_mass100_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo5e+24_wdm1.25_pe10_eps0.007_mass100_cl.dat']

data1 = []
data2 = []
for data_file in files1:
    data1.append(np.loadtxt(data_file))

for data_file in files2:
    data2.append(np.loadtxt(data_file))


roots = ['Planck2018',
'$\\tau$ = 1e+20 s',
'$\\tau$ = 5e+20 s',
'$\\tau$ = 5e+21 s', 
'$\\tau$ = 5e+22 s',
'$\\tau$ = 5e+23 s',
'$\\tau$ = 5e+24 s']  #Gyr


fig, ax = plt.subplots(2, sharex=True, sharey=True)

y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

color = ['goldenrod','blue', 'green','chocolate', 'orangered', 'orchid', 'orange', 'magenta','red']


index0, curve0 = 0, data1[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax[0].semilogx(curve0[:, 0], abs(curve0[:, 1]), color='black', linewidth = 2.2)
ax[1].semilogx(curve0[:, 0], abs(curve0[:, 1]), color='black', linewidth = 2.2)

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
    ax[0].semilogx(curve[:, 0], abs(curve[:, 1]), color = color[idx],linestyle=(0,(5,1)) , linewidth=1.7)

ax[0].set_title("Bino mass 100, 300 GeV, $\\tau_{exo}$ varied ", loc='center')

for idx, dat in enumerate(data2[1:]):
    index, curve = idx, dat
    ax[1].semilogx(curve[:, 0], abs(curve[:, 1]), color = color[idx], linestyle=(0,(5,1)),linewidth=1.7)


fig.legend([root for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax[1].set_xlabel('$\ell$', fontsize=16)
ax[1].set_xlim(3,2700)

ax[0].annotate(r'Bino mass$= 100 GeV$', xy=(10.5, 8e-10))
ax[1].annotate(r'Bino mass$= 300 GeV$', xy=(10.5, 8e-10))

# plt.ylabel(r'$\frac{C_\ell^\mathrm{TT}(\Lambda\mathrm{DDM})}{C_\ell^\mathrm{TT}(\Lambda \mathrm{LCDM})}-1$',fontsize=15)
plt.ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=15)
# plt.title("$\Gamma$ varied , $\epsilon=0.0067$ ", loc='center')

# plt.savefig('wdm_eps_1208',dpi=300)
plt.show()
plt.clf()

