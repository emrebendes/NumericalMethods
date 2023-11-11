# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 08:56:56 2022

@author: EMRE BENDEŞ
"""

%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *

def graphic(f,x):
    fig, ax = plt.subplots()
    ax.plot(x,f(x))
    ax.set_aspect('equal')
    ax.grid() 
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')


graphic(lambda x:np.sin(10*x)+np.cos(3*x),np.arange(0,5,0.01) )

# graphic(lambda x:(667.38*(1-math.e**(-10*(x/68.1)))/x)-40,np.arange(4,20,0.01) )