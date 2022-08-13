import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo1e+20_wdm1.25_pe10_eps0.007_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/two_exo1e+20_wdm1.25_pe0.1_eps0.007_mass10_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['two_exo1e+20_wdm1', 'lcdm_cl', 'two_exo1e+20_wdm1']

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

index, curve = 2, data[2]
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