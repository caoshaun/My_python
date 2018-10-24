# -*- coding: utf-8 -*-

import numpy as np  #导入python的库函数
import scipy as sp
import pylab as pl
from scipy import signal
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#绘制sinx
#x=np.linspace(0,4*np.pi,100)
#pl.plot(x,np.sin(x))
#pl.show()

#绘制频率扫描图
# t=np.linspace(0,10,1000)
# x=signal.chirp(t,5,10,30)
# pl.plot(t,x)
# pl.show()

#绘制3D曲面图
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
Z=np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1, cstride=1, cmap='rainbow')
plt.show()
