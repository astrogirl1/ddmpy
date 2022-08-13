import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_lifetime/exo_tau3e10_pe10_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/thesis/exo_lifetime/exo_tau3e9_pe10_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['exo_tau3e10_pe10_cl', 'exo_tau3e9_pe10_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT', u'EE', u'TE', u'BB', u'phiphi', u'TPhi', u'Ephi']
tex_names = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

index, curve = 1, data[1]
y_axis = [u'TT', u'EE', u'TE', u'BB', u'phiphi', u'TPhi', u'Ephi']
tex_names = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()