# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:46:57 2023

@author: EMRE BENDEŞ
Aşağıdaki amaçlarla yazılmıştır:
- Taylor serisini polinom şeklindeki bir fonsiyon için açabilen taylor metodu 
- derste çözülen örnekdeki polinomu [0 1] aralığında 10 farklı değerini x0=0 noktası çevsesinde hesaplayarak X0 değerini belirlemek X değerine yaklaştğında hatanın azaldığını gözlemlemek 
"""

#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

from sympy import *

def taylor(n,x,x0):
    return sum([d[i](x0)*np.power((x-x0),i)/math.factorial(i) for i in range(n+1)])

coef = [-.1,-.15,-.5,-.25,1.2]
f = np.poly1d(coef)
d = [f.deriv(i) for i in range(len(coef))]

x = np.linspace(0, 1,11)

fig1 = plt.figure()
plt.plot(x,f(x),label="f1")
for n in range(len(coef)):   
    plt.plot(x,taylor(n,x,0), label="n="+str(n))
plt.grid()
plt.legend()
plt.show()








