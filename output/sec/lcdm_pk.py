import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_pk.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.6_eps0.0067_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['Planck2018', 
"$\Gamma_{wdm}^{-1}$ = 78.01 Gyr", 
"$\Gamma_{wdm}^{-1}$ = 55.27 Gyr", 
"$\Gamma_{wdm}^{-1}$ = 24.6 Gyr" ]

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

ax.legend([root for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

plt.ylabel(u'P(Mpc/h)^3',fontsize=15)
plt.title("$\Gamma$ varied, $\epsilon=0.0067$, P(k) vs k", loc='center')


ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()