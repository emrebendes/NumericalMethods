# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:37:41 2022

@author: EMRE BENDEŞ
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List
from math import *
from sympy import *


def graphic(freal,xdata):
    # xline=np.arange(min(xdata),max(xdata),0.01)
    xline=np.arange(0,1,0.01)
    # xline=np.arange(-5,10,0.01)
    f=freal+x  
    
    fig, ax = plt.subplots()
    ax.plot(xline,lambdify(x,freal)(xline))
    ax.plot(xline,lambdify(x,f)(xline))
    ax.plot(xline,xline)
    for i in range(len(xdata)-2):
        # ax.arrow(xdata[i],xdata[i+1],xdata[i+1]-xdata[i] , 0,width=.001)
        ax.plot([xdata[i],xdata[i+1]],[xdata[i+1],xdata[i+1]],linestyle='dashed', color="black")
        ax.plot([xdata[i+1],xdata[i+1]],[xdata[i+1],xdata[i+2]],linestyle='dashed', color="black")
    # ax.plot(xdata,y2,'ro')
    # ax.plot(y2,y2,'bo')
    # linestyle='dashed'
    
    ax.set_aspect('equal')
    ax.grid() 
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
def iteration(freal, x0, min_error=0.5, max_iteration=60):
    f=freal+x    
    i = 0
    Ea = 1
    xp = []
    xn = None
    print("\t  g(x) \t\t\t Ea " )
    while Ea > min_error and i < max_iteration:
        xn = lambdify(x,f)(x0)
        Ea = abs((xn -x0)/xn)*100
        print("%d - %2.8f \t %2.8f " % (i,xn,Ea) ) 
        x0 = xn
        xp.append(x0)
        i += 1
    # print(xp)
    return xp

def main():
    # fx = input("Write function: ")
    # given_function = lambda x: eval(fx)
    
    # f=e**(-x)-x
    # x1 = iteration(f, 0)    
    f=sin(x**.5)-x
    x1 = iteration(f, 0.5)    
    graphic(f,x1)

if __name__ == '__main__':
    x=Symbol('x')
    main()