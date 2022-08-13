import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.5_eps0.0067_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.45_eps0.0067_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['wdm_gam1', 'wdm_gam1', 'wdm_gam1', 'wdm_gam1']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 1, data[1]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 2, data[2]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 3, data[3]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()