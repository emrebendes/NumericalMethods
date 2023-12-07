# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 17:16:41 2022

@author: EMRE BENDEŞ
"""

#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

maxiter=50
A= np.array([[4,-1,-1],[6,8,0],[-5,0,12]])
x= np.array([2,3,7],dtype=np.double)
B= np.array([-2,45,80])

nto=4
to=0.05#10**-(nto+1)#♥0.00001
hata = True

ps=len(np.diag(A))
k=1
print("\t"+"\t\t\t".join(' x%d' % item for item in range(1,len(x)+1))+"\t\t\t"+"\t\t\t".join('E%d' % item for item in range(1,len(x)+1)) )
while k<maxiter and hata:
    tx=[]
    h=[]
    ht=True
    for i in range(ps):
        top=0
        for j in range(ps):
            if i!=j:
                top+=A[i,j]*x[j]
        tx.append((1/A[i,i])*(B[i]-top))
        # h.append(abs((tx[i]-x[i])/tx[i]))
        h.append(abs(tx[i]-x[i]))
        ht &= h[i]<to
    hata&=not ht
    x=tx
    # print("%d \t " % (k)+"\t ".join(map(str,tx))+"\t"+"\t".join(map(str,h)) ) 
    print("%d \t " % (k)+"\t ".join('%0.6f' % item for item in tx)+"\t"+"\t".join('%0.6f' % item for item in h) ) 
    k+=1
                
