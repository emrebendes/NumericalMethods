# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:53:03 2022

@author: EMRE5
"""

# %matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *
from scipy.interpolate import lagrange

def newton_divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

    return coef

def newton_polynomial(x_data, y_data, x):
    coef =newton_divided_diff(x_data, y_data)
    a = coef[0,:]
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p,coef
  
    
if __name__ == '__main__':    
    # x = np.array([-5, -1, 0, 2])
    # y = np.array([-2, 6, 1, 3])
    x=np.array([1,4,5,7])
    y=np.array([2,4,6,7])
    
    x_new=np.arange(min(x)-1,max(x)+1,0.01)
    
    
    #Lagrange interpolasyon polinomu
    f=lagrange(x, y)
    f2=lagrange(x[[0,1,3]], y[[0,1,3]])
    fig = plt.figure(figsize = (10,8))
    plt.plot(x_new, f(x_new), 'b',x_new, f2(x_new), 'y', x, y, 'ro')
    plt.title('Lagrange Polynomial')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    print(f(3.5))
    #Newton bölünmüş farklar interpolasyon polinomu
    y_new ,a= newton_polynomial(x, y, x_new)    
    print (a)
    y_new2 ,a= newton_polynomial(x[[0,1,3]], y[[0,1,3]], x_new) 
    plt.figure(figsize = (12, 8))
    plt.plot(x, y, 'bo')
    plt.plot(x_new, y_new, 'b',x_new, y_new2, 'y')
    plt.title('Newton Polynomial')
    plt.grid()
    # plt.plot(x_new, y_true)   
    
    
    # y_new ,a= newton_polynomial(x, y, 2)
    # y=np.log(2)
    
    # print(y_new)
    # e=abs((y-y_new)/y)*100
    # print(e)
    
    