from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/lcdm_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_gamexo1e-1_pe0.1_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_gamexo1e-3_pe0.1_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_gamexo1e-4_pe0.1_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_gamexo1e-7_pe0.1_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
# roots = ['lcdm', '$\Gamma_{exo}$=1e-1', '$\Gamma_{exo}$=1e-3', '$\Gamma_{exo}$=1e-4', '$\Gamma_{exo}$=1e-7'] #km/s/Mpc
roots = ['lcdm', '$\Gamma_{exo}$=1e-9', '$\Gamma_{exo}$=1e-7', '$\Gamma_{exo}$=1e-5', '$\Gamma_{exo}$=1e-4'] #Gyr
# roots = ['lcdm', '$\gamma$=0.1', '$\gamma$=1e-7', '$\gamma$=1e-5', '$\gamma$=1e-4'] #Gyr

fig, ax = plt.subplots()

index0, curve0 = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
# ax.semilogx(curve0[:, 0], (curve0[:, 1])/(curve0[:, 1])-1, color='black')
ax.loglog(curve0[:, 0], abs(curve0[:, 1]), color='black', linestyle='dashed')
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index1, curve1 = 1, data[1]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
# ax.semilogx(curve1[:, 0], (curve0[:, 1]/curve1[:, 1])-1, color='red')
ax.loglog(curve1[:, 0], abs(curve1[:, 1]), color='green')
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index2, curve2 = 2, data[2]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
# ax.semilogx(curve2[:, 0], (curve0[:, 1]/curve2[:, 1])-1, color='green')
ax.loglog(curve2[:, 0], abs(curve2[:, 1]), color='red')
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index3, curve3 = 3, data[3]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
# ax.semilogx(curve3[:, 0], (curve0[:, 1]/curve3[:, 1])-1, color='rebeccapurple', linestyle='dashed')
ax.loglog(curve3[:, 0], abs(curve3[:, 1]))
# ax.loglog(curve[:, 0], abs(curve[:, 3]))

index4, curve4 = 4, data[4]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
# ax.semilogx(curve4[:, 0], (curve0[:, 1]/curve4[:, 1])-1, color='lightcoral', linestyle='dashed')
ax.loglog(curve4[:, 0], abs(curve4[:, 1]),linestyle='dashed')
# ax.loglog(curve[:, 0], abs(curve[:, 3]))


ax.legend([root+' Gyr' for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
# plt.ylabel(r'$\frac{C_\ell^\mathrm{TT}(\Lambda \mathrm{DDM})}{C_\ell^\mathrm{TT}(\Lambda \mathrm{LCDM})}-1$',fontsize=15)
plt.ylabel(r'$C_\ell^\mathrm{TT}(\Lambda \mathrm{DDM})$',fontsize=15)
plt.title("$\Gamma$ varied, photon energy = 0.1 GeV ", loc='center')
plt.show()
