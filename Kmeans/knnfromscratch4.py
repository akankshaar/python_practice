# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:06:26 2019

@author: Rhea Arora
"""

import numpy as np
import matplotlib.pyplot as pt
data = 10+(50-10)*np.random.random((2,1000))
np.round(data)
c1x=data[0,0];c1y=data[1,0]
c2x=data[0,1];c2y=data[1,1]
c3x=data[0,2];c3y=data[1,2]
c4x=data[0,3];c4y=data[1,3]
pt.ion()
pt.figure(1)
for j in range(30):
    c11x=[];c11y=[];c22x=[];c22y=[];c33x=[];c33y=[];c44x=[];c44y=[]
    pt.cla()
    for i in range(1000):
        d1=np.sqrt((data[0,i]-c1x)**2+(data[1,i]-c1y)**2)
        d2=np.sqrt((data[0,i]-c2x)**2+(data[1,i]-c2y)**2)
        d3=np.sqrt((data[0,i]-c3x)**2+(data[1,i]-c3y)**2)
        d4=np.sqrt((data[0,i]-c4x)**2+(data[1,i]-c4y)**2)
        #print(d1,d2,d3,d4)
        if d1<=d2 and d1<d3 and d1<d4:
            c11x.append(data[0,i])
            c11y.append(data[1,i])
            pt.plot(data[0,i],data[1,i],'ro')
        elif d2<d1 and d2<d3 and d2<d4:
            c22x.append(data[0,i])
            c22y.append(data[1,i])
            pt.plot(data[0,i],data[1,i],'bd')
        elif d3<d2 and d3<=d4 and d3<d1:
            c33x.append(data[0,i])
            c33y.append(data[1,i])
            pt.plot(data[0,i],data[1,i],'ms')
        else:
            c44x.append(data[0,i])
            c44y.append(data[1,i])
            pt.plot(data[0,i],data[1,i],'yo')
    pt.plot(c1x,c1y,'ks')
    pt.plot(c2x,c2y,'ks')
    pt.plot(c3x,c3y,'ks')
    pt.plot(c4x,c4y,'ks')
    c1x=sum(c11x)/len(c11x)
    c1y=sum(c11y)/len(c11y)
    c2x=sum(c22x)/len(c22x)
    c2y=sum(c22y)/len(c22y)
    c3x=sum(c33x)/len(c33x)
    c3y=sum(c33y)/len(c33y)
    c4x=sum(c44x)/len(c44x)
    c4y=sum(c44y)/len(c44y)
    pt.title('iter'+str(j+1))
    pt.pause(0.3)