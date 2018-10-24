# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4,5,0.15)
Y = np.arange(-4,4,0.15)
X,Y = np.meshgrid(X,Y)

#sigma1&2>0, -1<rho<1
mu1 = 2#int(input("请输入mu1"))
mu2 = -2#int(input("请输入mu2"))
sigma1 = 1#int(input("请输入sigma1"))
sigma2 = 1#int(input("请输入sigma2"))
rho1 = 0.1#int(input("请输入rho"))
a = 2*np.pi * sigma1*sigma2*(1-(rho1)**(2))**(1/2)
b = -(2*(1-rho1*rho1))**(-1)
c = ((X-mu1)/sigma1)**(2)
d = 2*rho1*(X-mu1)*(Y-mu2)*((sigma1*sigma2))**(-1)
f = ((Y-mu2)/sigma2)**(2)
Z = (1/a)*np.e**(b*(c-d+f))
#Z=np.e**((-0.5)*(X**(2)+Y**(2)))

ax.plot_surface(X,Y,Z,rstride=1, cstride=1, cmap='rainbow')
plt.show()
