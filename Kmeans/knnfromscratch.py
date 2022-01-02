# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:28:40 2019

@author: Rhea Arora
"""

import numpy as np
import matplotlib.pyplot as plt
data= 10+(50-10)*np.random.random((2,1000)) # because we want range 10 to 50 and 2 rows and 1000 columns
np.round(data)
c1x=data[0,0];c1y=data[1,0]
c2x=data[0,1];c2y=data[1,1]
plt.ion()
plt.figure()

for j in range(40):
   c11x=[]; c11y=[]
   c22x=[]; c22y=[]
   plt.cla()
   for i in range(0,1000):
       d1=np.sqrt((data[0,i]-c1x)**2+ (data[1:i]-c1y)**2)
       d2=np.sqrt((data[0,i]-c2x)**2+ (data[1:i]-c2y)**2)
       
       if d1<=d2:
           c11x.append(data[0,i])
           c11y.append(data[1,i])
           plt.plot(data[0,i], data[1,i], 'ro')
       elif d2<d1:
           c22x.append(data[0,i])
           c22y.append(data[1,i])
           plt.plot(data[0,i], data[1,i], 'bd')
plt.plot(c1x, c1y,'ks')
plt.plot(c2x, c2y,'ks')
c1x=sum(c11x)/len(c11x)
c1y=sum(c11y)/len(c11y)
c1x=sum(c22x)/len(c22x)
c1y=sum(c22y)/len(c22y)
plt.title('iter'+str(j+1))
plt.pause(0.3)

           
