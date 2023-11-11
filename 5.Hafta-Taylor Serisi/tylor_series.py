# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:33:37 2022

@author: EMRE BENDEŞ
Aşağıdaki amaçlarla yazılmıştır:
- Taylor serisini herhangi bir fonsiyon için açabilen taylor metodunu sympy kütüphanesi ile gerçekleştirme 
- KArekök fonksiyonunda her zaman küçük h=|x-x0| değeri için çabuk yakınsama olmadığını gözlemlemek. 
    örn: 2'0.5 için x0=4 (h=2) ile 11 iterasyonda yakınsama var iken x0=1 (h=1) ile 150 iterasyon yetersiz kalmakta.
"""
#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

from sympy import *


def taylor(f,n,x0,x_data):
    return sum([lambdify(x,f.diff(x,i))(x0)*np.power(x_data-x0,i)/math.factorial(i) for i in range(n+1)])

x=Symbol('x')
# f=E**x
# f=sin(x)
# f=-.1*x**4 -.15*x**3 -.5*x**2 -.25*x + 1.2
f=x**.5
x0=1#¨np.ones(11)*0
x_data = 2
anlamlı_basamak = 4
Es= 10**-(anlamlı_basamak+1)
Ea=10 # döngüye girmesi için rastgele büyük bir değer atanıyor.
n=0
ty=0
MAX_ITER=150
print("    taylor \t\t Ea \t\t\t Es") 
while(Es<Ea and n<MAX_ITER):
    tyn=taylor(f,n,x0,x_data)
    # ty+lambdify(x,f.diff(x,n))(x0)*np.power(x_data-x0,n)/math.factorial(n)
    Ea=abs(tyn-ty)
    ty=tyn
    print("%d \t %2.8f \t %2.8f \t %2.8f" % (n,ty,Ea,Es) ) 
    n+=1


x_data=np.linspace(0,1,11)
fig3= plt.figure()
#plt.plot(x_data,math.e**x_data,label="f1")
plt.plot(x_data,lambdify(x,f)(x_data),label="f1")
for n in range(5):   
    plt.plot(x_data,taylor(f,n,x0,x_data), label="n="+str(n))
plt.grid()
plt.legend()
plt.show()
