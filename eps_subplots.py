from turtle import color
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import itertools


# files = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam0.9_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.1_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.15_eps0.0067_cl.dat' ,
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.3_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.45_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.6_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.75_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.9_eps0.0067_cl.dat',
# '/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.93_eps0.0067_cl.dat']

files1 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.001_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.003_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.005_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.007_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.009_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.01_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.015_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.02_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/wdm_gam1.25_eps0.025_cl.dat']

files2 = ['/home/a1705053/Desktop/merged/merged_codes_may22/output/sec/lcdm_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.001_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.003_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.005_cl.dat' ,
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.007_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.009_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.01_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.015_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.02_cl.dat',
'/home/a1705053/Desktop/merged/merged_codes_may22/output/wdm_eps/wdm_gam1.47_eps0.025_cl.dat']

data1 = []
data2 = []
for data_file in files1:
    data1.append(np.loadtxt(data_file))

for data_file in files2:
    data2.append(np.loadtxt(data_file))


# roots = ['lcdm', '$\Gamma_{exo}$=1e-1', '$\Gamma_{exo}$=1e-3',
# '$\Gamma_{exo}$=1e-4', '$\Gamma_{exo}$=1e-7'] #km/s/Mpc
#roots = ['lcdm', 'tau = 3e9', 'tau = 1e10', 'tau = 3e10', 'tau = 1e11'] #Gyr
# roots = ['Planck2018',
# '$\Gamma^{-1}$ = 123.8 ',
# '$\Gamma^{-1}$ = 78.01 ',
# '$\Gamma^{-1}$ = 55.27 ', 
# '$\Gamma^{-1}$ = 49.26 ',
# '$\Gamma^{-1}$ = 34 ',
# '$\Gamma^{-1}$ = 24.64 ',
# '$\Gamma^{-1}$ = 17.48 ',
# '$\Gamma^{-1}$ = 12.38 ',
# '$\Gamma^{-1}$ = 11.54 ']  #Gyr

# roots = ['Planck2018',
# '$\epsilon$ = 0.001 ',
# # '$\epsilon$ = 0.005 ',
# '$\epsilon$ = 0.0067 ', 
# '$\epsilon$ = 0.01',
# '$\epsilon$ = 0.015 ',]
# # '$\epsilon$ = 0.02 ',
# # '$\epsilon$ = 0.025 ']
# # '$\epsilon$ = 12.38 ',
# # '$\epsilon$ = 11.54 ']  

roots = ['Planck2018',
'$\epsilon$ = 0.001 ',
'$\epsilon$ = 0.003 ',
'$\epsilon$ = 0.005 ', 
'$\epsilon$ = 0.007 ',
'$\epsilon$ = 0.009 ',
'$\epsilon$ = 0.01  ',
'$\epsilon$ = 0.015  ',
'$\epsilon$ = 0.02  ',
'$\epsilon$ = 0.025 ']  

# eps = [0, 0.001, 0.0067, 0.01, 0.015]
eps = [0, 0.001, 0.003, 0.005, 0.007, 0.009, 0.01, 0.015, 0.02, 0.025]
# fig, ax = plt.subplots()

fig, ax = plt.subplots(2, sharex=True, sharey=True)

y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []

color = ['goldenrod','blue', 'green','chocolate', 'orangered', 'orchid', 'orange', 'magenta','red']

# color = ['black', 'goldenrod','orange', 'darkorange', 'red', 'blueviolet']

index0, curve0 = 0, data1[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax[0].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2)
ax[1].semilogx(curve0[:, 0], (curve0[:, 1]), color='black', linewidth = 2.2)

for idx, dat in enumerate(data1[1:]):
    index, curve = idx, dat
    ax[0].semilogx(curve[:, 0], ((curve[:, 1]/curve0[:, 1])-1), color = color[idx] , linewidth=1.7)

ax[0].set_title("$\epsilon$ varied, $\Gamma_{wdm}$ constant ", loc='center')

for idx, dat in enumerate(data2[1:]):
    index, curve = idx, dat
    ax[1].semilogx(curve[:, 0], ((curve[:, 1]/curve0[:, 1])-1), color = color[idx],linewidth=1.7)
    # ax.semilogx(curve[:, 0], abs(curve[:, 1]), color = color[idx])
    # ax.semilogx(curve[:, 0], abs(curve[:, 1]),  c=cm.viridis(eps[idx]/(0.85*max(eps))), linestyle='dashdot', linewidth = 2)


fig.legend([root for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax[1].set_xlabel('$\ell$', fontsize=16)
ax[1].set_xlim(3,2700)

# ax[0].annotate(r'$\Gamma_{wdm}^{-1} = 55 Gyr$', xy=(10.5, 8e-10))
# ax[1].annotate(r'$\Gamma_{wdm}^{-1} = 30 Gyr$', xy=(10.5, 8e-10))

# plt.ylabel(r'$\frac{C_\ell^\mathrm{TT}(\Lambda\mathrm{DDM})}{C_\ell^\mathrm{TT}(\Lambda \mathrm{LCDM})}-1$',fontsize=15)
plt.ylabel(r'$C_\ell^\mathrm{TT}$',fontsize=15)
# plt.title("pe varied, $\Gamma_{exo}$ = 1e-2 km/s/Mpc ", loc='center')
# plt.title("$\Gamma$ varied , $\epsilon=0.0067$ ", loc='center')

# plt.savefig('wdm_eps_1208',dpi=300)
plt.show()
plt.clf()



# index0, curve0 = 0, data[0]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# # ax.semilogx(curve0[:, 0], (curve0[:, 1])/(curve0[:, 1])-1, color='black')
# ax.loglog(curve0[:, 0], abs(curve0[:, 1]), color='black')
# # ax.loglog(curve[:, 0], abs(curve[:, 3]))

# index1, curve1 = 1, data[1]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# # ax.semilogx(curve1[:, 0], (curve0[:, 1]/curve1[:, 1])-1, color='red')
# ax.loglog(curve1[:, 0], abs(curve1[:, 1]), color='goldenrod')
# # ax.loglog(curve[:, 0], abs(curve[:, 3]))

# index2, curve2 = 2, data[2]
# y_axis = [u'TT']
# tex_names = ['TT']
# x_axis = 'l'
# ylim = []
# xlim = []
# # ax.semilogx(curve2[:, 0], (curve0[:, 1]/curve2[:, 1])-1, color='green')
# ax.loglog(curve2[:, 0], abs(curve2[:, 1]), color='orange')
# # ax.loglog(curve[:, 0], abs(curve[:, 3]))

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



