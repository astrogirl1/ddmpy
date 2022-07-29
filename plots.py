from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/lcdm_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam0.05_eps0.0068_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam69_eps0.0068_gamexo0.0005_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/wdm1_gam69_eps0.0068_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['lcdm', '$\Gamma_{wdm}$=0.05', '$\Gamma_{wdm}$=69+0.0005', '$\Gamma_{wdm}$=69']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], abs(curve[:, 1]), color='black')
# ax.loglog(curve[:, 0], abs(curve[:, 2]))
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index, curve = 1, data[1]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], abs(curve[:, 1]), color='red')
# ax.loglog(curve[:, 0], abs(curve[:, 2]))
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index, curve = 2, data[2]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], abs(curve[:, 1]), color='green')
# ax.loglog(curve[:, 0], abs(curve[:, 2]))
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index, curve = 3, data[3]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], abs(curve[:, 1]))
# ax.loglog(curve[:, 0], abs(curve[:, 2]))
# ax.loglog(curve[:, 0], abs(curve[:, 3]))


ax.legend([root for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.ylabel(r'$C_\ell^\mathrm{TT}(\Lambda \mathrm{DDM})$',fontsize=15)
plt.title("$\Gamma$ varied, photon energy = 0.1 GeV ", loc='center')
plt.show()
