# -*- coding: utf-8 -*-
"""
Created on Fri May 12 03:17:29 2017

@author: User
"""

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

f = open("chonchi.txt")
string = f.read().split("\n")
ancho = [x.split(" ")[0] for x in string]
alto = [x.split(" ")[1] for x in string]
ancho = [float(x) for x in ancho]
alto = [float(x) for x in alto]


plt.plot(ancho,alto)
plt.grid(True)
plt.hold(True)
horiz_line_data = np.array([1.66 for i in range(len(ancho))])
plt.plot(ancho, horiz_line_data, 'r--') 

ancho2 = np.linspace(ancho[0],ancho[-1],10000)
ff = interp1d(ancho,alto)
alto2 = ff(ancho2)
plt.figure()
plt.plot(ancho2,alto2,'g')
plt.grid()
horiz_line_data = np.array([1.66 for i in range(len(ancho2))])
plt.plot(ancho2, horiz_line_data, 'r--') 
plt.show

plt.figure()
plt.grid
alto3 = -alto2 + horiz_line_data
alto3 = [0 if x<=0 else x for x in alto3]
plt.plot(ancho2,alto3,'c')
plt.show()
print(np.trapz(alto3,ancho2))
