# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:48:16 2019

@author: Rhea Arora
"""

import numpy as np
import matplotlib.pyplot as plt
data= 10+(50-10)*np.random.random((2,1000)) # because we want range 10 to 50 and 2 rows and 1000 columns
data=np.round(data)
plt.figure(1)
plt.subplot(2,1,1) #subplot to avoid overlapping
plt.plot(data[0,:], data[1,:],'b*')
plt.subplot(2,1,2)

for i in range(0,1000):
    if(data[0,i]>=20 and data[0,i]<30):
        plt.plot(data[0,i], data[1,i],'go')
    elif(data[0,i]<20):
        plt.plot(data[0,i], data[1,i],'ko')        
    elif(data[0,i]>=30 and data[0,i]<40):
        plt.plot(data[0,i], data[1,i],'md')
    else:
        plt.plot(data[0,i],data[1,i],'rd')
plt.show()