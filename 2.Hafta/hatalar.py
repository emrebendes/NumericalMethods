#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt


def f(x): #e^-1+ln(x) fonksiyonu
    return np.power(math.e,-1*x)+np.log(x)

def plot(n0,n1):# verilen aralıkta f(x) fonksiyonunu 100 değer ile çalıştırıp o aralıkta grafik çiziyor.
    x=np.linspace(n0,n1,101)
    s= f(x)
    plt.plot(x,s)
    plt.grid()
    plt.xticks(np.arange(n0,n1,(n1-n0)/10))
    plt.show()

def bul():#0-10 aralığında fonksiyonun nerede işret değiştirdiğini arıyor.
    x=np.linspace(0,10,101)
    y= f(x)
    limits=np.array([[0,10]])
    
    for i in range(5):
        m=y[1:-1]*y[0:-2]
        ind=np.argwhere(m<0)[0][0]
        n0=x[ind]
        n1=x[ind+1]
        limits=np.concatenate((limits,[[n0,n1]]))
        x=np.linspace(n0,n1,101)
        y= f(x)
    return limits
 
def ex(x,n):#maclourin açılımını x değeri için n elemanla hesaplıyor.
    # s=0;
    # for i in range(n):
    #     s+=x**i/math.factorial(i)
    # return s
    return sum([x**i/math.factorial(i) for i in range(n)])


# 10 iterasyon maclourin açılımı açıp gerçek ve yaklaşık hataları hesaplayarak tablo hlinde ekrana bastır
print("   Sonuç \t\t\t Et \t\t\t Ea") 
snc=[];
gd=math.e**0.5
for i in range(1,10):
    snc.append(ex(0.5,i))
    if i>1:
        et = abs((gd-snc[-1])/gd)*100
        ea = abs((snc[-1]-snc[-2])/snc[-1])*100
        print("%d - %1.8f \t %1.8f \t %1.8f" % (i,snc[-1],et,ea) ) 
       
# ex(2)
# limit=bul()   

#  e^-1+ln(x) fonksiyonunu farklı aralıklarda deneyerek grafiğini çiz ve sürekli bir hata olduğunu gözlemle ...
plot(.5,.6)