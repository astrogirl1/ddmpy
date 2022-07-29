import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/ex1_merged_G4e-6_df1_pe0.001_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/ex1_merged_G4e-6_df0.2_pe0.001_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['ex1_merged_G4e-6_df1_pe0', 'ex1_merged_G4e-6_df0']

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

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()