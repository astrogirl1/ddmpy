from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/lcdm_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam0.05_eps0.0068_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam17.77_eps0.0068_gamexo0.065_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam69_eps0.0068_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['lcdm', '$\Gamma_{wdm}$=0.05', '$\Gamma_{wdm}$=17.77', '$\Gamma_{wdm}$=69']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]), color='black')


index, curve = 1, data[1]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]), color='red')

index, curve = 2, data[2]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]), color='green')


index, curve = 3, data[3]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))



ax.legend([root+' km/s/Mpc' for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.ylabel(r'P(k)',fontsize=15)
plt.xlabel(r'k',fontsize=15)

plt.title("$\Gamma$ varied, photon energy = 0.1 GeV ", loc='center')
plt.show()
