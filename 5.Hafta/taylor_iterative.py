# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:51:30 2022

@author: EMRE BENDEŞ
Aşağıdaki amaçlarla yazılmıştır:
- Taylor serisini herhangi bir fonsiyon için açabilen taylor metodunu sympy kütüphanesi ile gerçekleştirme 
- KArekök fonksiyonunda her zaman küçük h=|x-x0| değeri için çabuk yakınsama olmadığını gözlemlemek. 
    örn: 2'0.5 için x0=4 (h=2) ile 11 iterasyonda yakınsama var iken x0=1 (h=1) ile 150 iterasyon yetersiz kalmakta.
- taylor_serries dosyasına göre temel fark sadece serinin fonksiyonda değilde döngü içerisinde hesaplanıyor oluşu
"""
#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *



MAX_ITER=150
x=Symbol('x')
f=x**.5
# f=E**x
# f=cos(x)
# x0=4

x0= 4#math.pi/8

x_data=2#0.4141#math.pi/7
anlamlı_basamak = 4
Es= 10**-(anlamlı_basamak+1)
Ea=10
n=0
ty=0

print("    taylor \t\t Ea \t\t\t Es") 
while(Es<Ea and n<MAX_ITER):
    tyn=ty+lambdify(x,f.diff(x,n))(x0)*np.power(x_data-x0,n)/math.factorial(n)
    Ea=abs(tyn-ty)
    ty=tyn
    print("%d \t %2.8f \t %2.8f \t %2.8f" % (n,ty,Ea,Es) ) 
    n+=1
    
