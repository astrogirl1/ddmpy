from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import itertools


# files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.3_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.45_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.6_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.75_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.9_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.93_eps0.0067_cl.dat',]

# files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/january/lcdm_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.001_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.01_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.1_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/gamma_eps0.5_cl.dat']


# files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/january/lcdm_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/eps_gam100_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/eps_gam30_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/eps_gam10_cl.dat']
# files1= ['/home/a1705053/Desktop/merged/merged_codes_may22/january/lcdm_cl.dat', '/home/a1705053/Desktop/merged/merged_codes_may22/january/residual_2_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/exoclass_2_cl.dat']
# files2= ['/home/a1705053/Desktop/merged/merged_codes_may22/january/exoclass_lcdm_cl.dat','/home/a1705053/Desktop/merged/merged_codes_may22/january/exoclass_1_cl.dat']

files2 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.001_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.003_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.005_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.007_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.009_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.01_cl.dat',]
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.015_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.02_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.025_cl.dat']

data1 = []

for data_file in files1:
    data1.append(np.loadtxt(data_file))

# roots = ['Planck2018', 
# "$\Gamma_{wdm}^{-1}$ = 78.01 Gyr", 
# "$\Gamma_{wdm}^{-1}$ = 55.27 Gyr", 
# "$\Gamma_{wdm}^{-1}$ = 24.6 Gyr" ]

fig, ax = plt.subplots()

y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

color = ['goldenrod','blue', 'green','chocolate', 'orangered', 'orchid', 'orange', 'magenta','red']


index0, curve0 = 0, data1[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 1.5)

# index1, curve1 = 0, data2[0]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.semilogx(curve1[:, 0], (curve1[:, 1]), color='blue', linewidth = 1.2)

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
    ax.semilogx(curve[:, 0], ((curve[:, 1]/curve0[:, 1])-1), color = color[idx] , linewidth=1.8, linestyle='dashed')

# fig.legend([root for (root, elem) in
#     itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=20)
ax.set_xlim(3,2700)

# ax[0].annotate(r'$\Gamma_{wdm}^{-1} = 55 Gyr$', xy=(10.5, 8e-10))
ax.tick_params(labelsize=18)

plt.ylabel(r'$\frac{C_\ell^\mathrm{TT}(\Lambda\mathrm{DDM})}{C_\ell^\mathrm{TT}(\Lambda \mathrm{CDM})}-1$',fontsize=20)
# plt.ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=15)
# plt.title("pe varied, $\Gamma_{exo}$ = 1e-2 km/s/Mpc ", loc='center')
# plt.title("$\Gamma$ varied , $\epsilon=0.0067$ ", loc='center')
plt.legend([r'$\Lambda$CDM', r'$\epsilon=0.001$',r'$\epsilon=0.01$', r'$\epsilon=0.1$', r'$\epsilon=0.5$'])
# plt.legend([r'$\Lambda$CDM', r'Modified CLASS(2023) $(10^{22}s)$',r'ExoCLASS $(10^{22}s)$'], fontsize=18, loc='upper left')
# plt.title(r'Exoclass vs Merged Code', loc='center')
# plt.savefig("residual_2_gamwdm1e-10kmsMpc.pdf", format="pdf")
plt.savefig("chap4epsilon.pdf", format="pdf")


plt.show()
plt.clf()


# index3, curve3 = 3, data[3]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# # ax.semilogx(curve3[:, 0], (curve0[:, 1]/curve3[:, 1])-1,
# # color='rebeccapurple', linestyle='dashed')
# ax.loglog(curve3[:, 0], abs(curve3[:, 1]),color='darkorange')
# # ax.loglog(curve[:, 0], abs(curve[:, 3]))

# index4, curve4 = 4, data[4]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve4[:, 0], abs(curve4[:, 1]), color='mediumorchid')

# index5, curve5 = 5, data[5]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve5[:, 0], abs(curve5[:, 1]), color='darkorchid')

# index6, curve6 = 6, data[6]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve6[:, 0], abs(curve6[:, 1]), color='darkviolet')

# index6, curve6 = 6, data[6]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve6[:, 0], abs(curve6[:, 1]), color='darkviolet')

# index6, curve6 = 6, data[6]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve6[:, 0], abs(curve6[:, 1]), color='darkviolet')


# index6, curve6 = 6, data[6]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# ax.loglog(curve6[:, 0], abs(curve6[:, 1]), color='darkviolet')



