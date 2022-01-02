# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:17:40 2019

@author: Rhea Arora
"""
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np

#Training data preparation
samp=7
train_data=np.zeros((7*40,10304))
train_label= np.zeros((7*40))
count=-1
#plt.figure(1)
#plt.ion()

for i in range(1,41):
    for j in range (1,samp+1):
        #plt.cla() #to clear axis
        count=count+1
        print(count)
        path="C:\\Users\\Rhea Arora\\Documents\\python\\\Face\\orl_face\\u%d\\%d.png"%(i,j)
        im=mimg.imread(path)
        feat=im.reshape(1,-1)
        train_data[count,:]=feat
        train_label[count]=i

#testing data preparation        
print(train_data)
print(train_label)
test_data=np.zeros(((10-samp)*40,10304))
test_label=np.zeros(((10-samp)*40))
count=-1

for i in range(1,41):
    for j in range(samp+1,11):
        #plt.cla()
        count=count+1
        path="C:\\Users\\Rhea Arora\\Documents\\python\\\Face\\orl_face\\u%d\\%d.png"%(i,j)
        im=mimg.imread(path)
        feat=im.reshape(1,-1)
        test_data[count,:]=feat
        test_label[count]=i
        
incorrect=0; 
correct=0;
for i in range(0,(10-samp)*40):
    test_sample=test_data[i,:]
    actual_label=test_label[i]
    d=np.zeros((samp*40))
    for j in range(0,samp*40):
        d[j]=np.sum((test_sample-train_data[j,:])**2)
        #take index of minimum distance
    val= d.min()
    ind=d.argmin()
    pred_op=train_label[ind]
    if pred_op==actual_label:
        correct=correct+1
    else:
        incorrect=incorrect+1
accuracy=(correct/(incorrect+correct))*100
print("accuracy = ", accuracy)
        