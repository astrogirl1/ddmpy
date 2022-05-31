import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged_codes_may22/output/poulin_tests/test1_poulin_only_recfast_cl.dat', '/home/a1705053/Desktop/merged_codes_may22/output/poulin_tests/test1_separate_poulin_recfast_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test1_poulin_only_recfast_cl', 'test1_separate_poulin_recfast_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
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
y_axis = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
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