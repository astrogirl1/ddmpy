from doctest import OutputChecker
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import itertools


files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output19/lcdm_hyrec_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.001_hyrec_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.01_hyrec_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.1_hyrec_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output19/merged_eps0.5_hyrec_cl.dat']


files2 = ['/home/a1705053/Desktop/1908/class_decays/output/eps0_hyrec_cl.dat',
# '/home/a1705053/Desktop/1908/class_decays/output/eps0.001_hyrec_cl.dat',
# '/home/a1705053/Desktop/1908/class_decays/output/eps0.01_hyrec_cl.dat',
'/home/a1705053/Desktop/1908/class_decays/output/eps0.1_hyrec_cl.dat',
'/home/a1705053/Desktop/1908/class_decays/output/eps0.5_hyrec_cl.dat']

data1 = []
data2 = []

for data_file in files1:
    data1.append(np.loadtxt(data_file))
for data_file in files2:
    data2.append(np.loadtxt(data_file))
roots = [r'$\Lambda$CDM', r'$\epsilon = 0.1$', r'$\epsilon = 0.5$']

# fig, ax = plt.subplots()

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

fig, (ax1,ax2) = plt.subplots(2)
##-------------------LCDM TT MERG----------------
index, curve= 0, data1[0]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax2.semilogx(curve[:, 0], abs(curve[:, 1]), color='black', linewidth=1.7, linestyle='dashed')
##-------------------LCDM TT ORIG----------------
index, curvE = 0, data2[0]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax1.semilogx(curve[:, 0], abs(curve[:, 1]), color='black', linewidth=1.7, linestyle='dashed')

ax1.set_xlim(5.3, 2740)
ax1.set_ylim(0.01e-10, 8e-10)
ax2.set_xlim(5.3, 2740)
ax2.set_ylim(0.01e-10, 8e-10)


##-----LCDM EE MERG ------------

# index1, curve1 = 0, data2[0]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax3.semilogx(curve1[:, 0], abs(curve1[:, 2]), color='black', linewidth=1.7, linestyle='dashed')

# ##---------LCDM EE ORIG ---------
# index1, curve1 = 0, data2[0]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax4.semilogx(curve1[:, 0], abs(curve1[:, 2]), color='black', linewidth=1.7, linestyle='dashed')

##-------eps 0.1 TT MERG------
index, curve= 1, data1[1]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax2.semilogx(curve[:, 0], abs(curve[:, 1]), color='red')

##-------eps 0.1 TT ORIG------
index, curve= 1, data2[1]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax1.semilogx(curve[:, 0], abs(curve[:, 1]), color='red')

##-------eps 0.1 EE MERG------
# index, curve= 1, data1[1]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax3.semilogx(curve[:, 0], abs(curve[:, 2]), color='red')

# ##-------eps 0.1 EE ORIG------
# index, curve= 1, data2[1]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax4.semilogx(curve[:, 0], abs(curve[:, 2]), color='red')



##-------eps 0.5 TT MERG------
index, curve= 2, data1[2]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax2.semilogx(curve[:, 0], abs(curve[:, 1]), color='blue')

##-------eps 0.5 TT ORIG------
index, curve= 2, data2[2]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax1.semilogx(curve[:, 0], abs(curve[:, 1]), color='blue')

##-------eps 0.5 EE MERG------
# index, curve= 2, data1[2]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax3.semilogx(curve[:, 0], abs(curve[:, 2]), color='blue')

# ##-------eps 0.5 EE ORIG------
# index, curve= 2, data2[2]
# y_axis = ['EE']
# tex_names = ['EE']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax4.semilogx(curve[:, 0], abs(curve[:, 2]), color='blue')


ax1.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')
plt.title(r"Example decay scenario comparisons for fixed $\Gamma^{-1} = 55 Gyr$")
ax2.set_title('(b) Merged')
ax1.set_title('(a) Original')

ax2.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax1.set_ylabel(r"$C_{l}^{TT}$")
ax2.set_ylabel(r"$C_{l}^{TT}$")
ax1.set_xlabel('$\ell$', fontsize=16)
ax2.set_xlabel('$\ell$', fontsize=16)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.suptitle(r"Merged Code vs Original Comparison for various $\epsilon$",x=0.56,y=0.95)
plt.show()