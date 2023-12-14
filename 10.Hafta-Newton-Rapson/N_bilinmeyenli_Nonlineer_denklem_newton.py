# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:17:48 2022

@author: EMRE BENDEŞ
Sembolik programlama kullanıldı.
"""


from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt

def iteration(F, X, x0, min_error=0.0000001, max_iteration=6):
    j = F.jacobian(X)
    h=False
    i = 0
    while not h and i < max_iteration:
        J = lambdify(X,j)(x0[0],x0[1])
        f = lambdify(X,F)(x0[0],x0[1])
        deltaX = np.linalg.solve(J,f)
        deltaX = np.squeeze(deltaX)
        xn= x0-deltaX
        Ea = abs(xn-x0)
        
        ht=true
        for e in Ea:
            ht&=e<min_error
        h|=ht
        x0=xn
        i += 1
        print("%d- "% (i)+" ".join('%0.8f' % item for item in x0))
        # print("%d- "% (i)+" ".join(map(str,x0)))
    
def main():
    x, y, z = symbols('x y z', real=True)
    f1 = x**2-2*x-y+.5#4*x*y + x*z + x**3 + z**8*y# 4*x*y + x*sin(z) + x**3 + z**8*y
    f2 = x**2+4*y**2-4#♣2*x*z + x + y**2 
    f3 = 4*x*y*z + y*z

    F=Matrix([f1,f2])
    X=Matrix([x,y])

    x0=2
    y0=.25

    iteration(F,X,np.array([x0,y0]))

if __name__ == '__main__':
    main()



 
# j = F.jacobian(X)
# J = lambdify(X,j)(x0,y0)
# f = lambdify(X,F)(x0,y0)
# deltaX = np.linalg.solve(J,f)

# x0=x0-deltaX[0]
# y0=y0-deltaX[1]

# dx=diff(f, x)
# dy=diff(f,y)
# lambdify([x,y,z], dx)(1,1,1)
