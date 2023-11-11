# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:33:37 2022

@author: EMRE BENDEŞ
"""
%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *

MAX_ITER =100
Es=.0001
Eapproximate=[]
Etrue=[]

def check(f,xa,xu):
    if f(xa)*f(xu)>0:
        return False
    else:
        return True

def Ea(xy,xe):
    return abs(100*(xy-xe)/xy)
def Et(x,r):
    return abs(100*(r-x)/r)

def bisection(f,xa,xu):
    if check(f, xa, xu):
        # fig2, ax = plt.subplots()       
        # xall=np.arange(xa,xu,0.01)
        # ax.plot(xall,f(xall))
        # ax.axhline(y=0, color='k')
        # ax.axvline(x=0, color='k')
        # ax.set_aspect('equal')
        # ax.grid()
        
        n=0
        stop = False
        xr= (xa+xu)/2
        print("\t  Xr \t\t\t F(Xr) \t\t\t Ea \t\t\t Et" )
        while(not stop and n<MAX_ITER):            
            
            # if n<5:
            #     ax.plot([xr,xu],[f(xr),f(xu)])
            
            if check(f,xr,xu):
                xa=xr
            else:
                xu=xr
            xry= (xa+xu)/2
                        
            E=Ea(xry,xr)
            Etrue.append(Et(xry,Xg))
            Eapproximate.append(E)
            print("%d \t- %2.8f \t %2.8f \t %2.8f \t %2.8f" % (n,xry,f(xry),E,Etrue[-1]) )  
            if Es<E:
                xr=xry
                n+=1
            else:
                stop=True
    else:
        print("verilen aralıkta bir kök yok..!")
        

# Xg=14.780205
# bisection(lambda x:(667.38*(1-math.e**(-10*(x/68.1)))/x)-40,12,16 )
Xg=1
bisection(lambda x:x**10-1,0,1.3 )

fig, ax = plt.subplots()
ax.plot(Etrue,label="gerçek bağıl hata")
ax.plot(Eapproximate,label="yaklaşık bağıl hata")
ax.set_aspect('equal')
ax.grid()
ax.legend()

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


