# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:57:46 2022

@author: EMRE5
"""
%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
 
def graphic3d(x,y,z,zt):    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(x, y, z)
    fig.show()

def graphic(x,y,yt):    
    fig, ax = plt.subplots()
    ax.plot(x,yt)
    ax.plot(x,y,'r.')
    ax.set_aspect('equal')
    ax.grid() 
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

def graphic(x,y,f):    
    fig, ax = plt.subplots()
    ax.plot(x,f(x))
    ax.plot(x,y,'r.')
    ax.set_aspect('equal')
    ax.grid() 
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
def lineer_regresyon_1d_m1(x,y):
    sx=sum(x)
    sxx=sum(x**2)
    sy=sum(y)
    sxy=sum(x*y)
    n=len(x)
    a1=(n*sxy-sx*sy)/(n*sxx-sx**2)
    a0=(sxx*sy-sxy*sx)/(n*sxx-sx**2)        
    print("sx=%d - sxx=%d - sy=%d - sxy=%d" % (sx,sxx,sy,sxy) ) 
    print("Birinci Yolla 1 Boyutlu Lineer Regresyon\ny = %2.4fx +  %2.4f " % (a1,a0) )
    yt=a1*x+a0
    return lambda x:a1*x+a0

def lineer_regresyon_1d_m2(x,y):    
    A=np.concatenate((np.expand_dims(x, axis=1),np.ones([len(x),1])),axis=1)
    AtA=np.matmul(A.transpose(),A)
    Atb=np.matmul(A.transpose(),y)
    [a1,a0]=np.linalg.solve(AtA,Atb)
    yt=a1*x+a0
    print("İkinci Yolla 1 Boyutlu Lineer Regresyon\ny = %2.4fx +  %2.4f " % (a1,a0) )
    return lambda x:a1*x+a0
    
def lineer_regresyon_1d_m3(x,y):  
    A = np.vstack([x, np.ones(len(x))]).T
    [a1,a0]=np.linalg.lstsq(A,y,rcond=None)[0]
    yt=a1*x+a0
    print("Üçüncü Yolla 1 Boyutlu Lineer Regresyon\ny = %2.4fx +  %2.4f " % (a1,a0) )
    return lambda x:a1*x+a0

def lineer_regresyon_1d_m4(x,y):  
    [a1,a0]=np.polyfit(x,y,1)
    yt=a1*x+a0
    print("Dördüncü Yolla 1 Boyutlu Lineer Regresyon\ny = %2.4fx +  %2.4f " % (a1,a0) )
    return lambda x:a1*x+a0


def polinom_regresyon_1d_m3(x,y,n):  
    A = np.vstack([x**i for i in range (n,-1,-1)]).T
    a=np.linalg.lstsq(A,y,rcond=None)[0]
    yt=np.poly1d(a)(x)
    print("%d Boyutlu Tek Tarametreli Polinom Regresyonu\n "%(n)+" - ".join(map(str,a)) )
    return lambda x:np.poly1d(a)(x)

def polinom_regresyon_1d_m4(x,y,n):  
    a=np.polyfit(x,y,n)
    yt=np.poly1d(a)(x)
    print("%d Boyutlu Tek Tarametreli Polinom Regresyonu\n "%(n)+" - ".join(map(str,a)) )
    return lambda x:np.poly1d(a)(x)

def lineer_regresyon_Nd_m3(x,y):  
    A = np.vstack([x, np.ones(len(x))]).T
    [a2,a1,a0]=np.linalg.lstsq(A,y,rcond=None)[0]
    yt=a2*x[:,1]+a1*x[:,0]+a0
    print("Üçüncü Yolla n Boyutlu Lineer Regresyon\ny = %2.4fx +  %2.4f " % (a1,a0) )
    return lambda x:a1*x+a0
    
def main(x,y):    
    if type(x)==list and type(y)==list:
        x=np.array(x)
        y=np.array(y)
 
    f=lineer_regresyon_1d_m1(x,y)
    graphic(x, y, f)
    
    f=lineer_regresyon_1d_m2(x,y)
    graphic(x, y, f)
    
    f=lineer_regresyon_1d_m3(x,y)
    graphic(x, y, f)
    
    f=lineer_regresyon_1d_m4(x,y)
    graphic(x, y, f)

if __name__ == '__main__':    
    # x=np.array([0,1,2,3,4,5])
    # y=np.array([2.1,7.7,13.6,27.2,40.9,61.1])
    # f=polinom_regresyon_1d_m3(x,y,2)
    # graphic(x, y, f)
        
    x= np.array([1,2,3,3,4,5,6,7,8,10])
    y= np.array([1,3,2,4,6,3,5,7,7,11])
    main(x,y)    





#Yöntem 1
# sx=sum(x)
# sxx=sum(x**2)
# sy=sum(y)
# sxy=sum(x*y)
# n=len(x)
# a1=(n*sxy-sx*sy)/(n*sxx-sx**2)
# a0=(sxx*sy-sxy*sx)/(n*sxx-sx**2)


# print("sx=%d - sxx=%d - sy=%d - sxy=%d" % (sx,sxx,sy,sxy) ) 
# print("Birinci Yolla \ny = %2.4fx +  %2.4f " % (a1,a0) )
# yt=a1*x+a0
# print(yt)
# graphic(x, y,yt)


#Yöntem 2
# A=np.concatenate((np.expand_dims(x, axis=1),np.ones([len(x),1])),axis=1)
# AtA=np.matmul(A.transpose(),A)
# Atb=np.matmul(A.transpose(),y)
# [a1,a0]=np.linalg.solve(AtA,Atb)
# yt=a1*x+a0
# print("İkinci Yolla \ny = %2.4fx +  %2.4f " % (a1,a0) )
# # print(yt)
# graphic(x, y,yt)


#yöntem3
# A = np.vstack([x, np.ones(len(x))]).T
# [a1,a0]=np.linalg.lstsq(A,y,rcond=None)[0]
# yt=a1*x+a0
# print("Üçüncü Yolla \ny = %2.4fx +  %2.4f " % (a1,a0) )
# # print(yt)
# graphic(x, y,yt)


#yöntem 4
# [a1,a0]=np.polyfit(x,y,1)
# yt=a1*x+a0
# print("Dördüncü Yolla \ny = %2.4fx +  %2.4f " % (a1,a0) )
# # print(yt)
# graphic(x, y,yt)