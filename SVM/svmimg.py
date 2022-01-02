# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:34:01 2019

@author: Rhea Arora
"""


import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
from sklearn import svm, metrics
from sklearn.metrics import confusion_matrix

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

#Linear kernel
svc_linear=svm.SVC(kernel ="linear", C=1)
svc_linear.fit(train_data,train_label)
y_pred=svc_linear.predict(test_data)
cnf_matrix= confusion_matrix(test_label, y_pred)
print(cnf_matrix)
ac1=metrics.accuracy_score(test_label,y_pred)
acc1=ac1*100
print(acc1)

#poly kernel
svc_linear=svm.SVC(kernel ="poly", C=1)
svc_linear.fit(train_data,train_label)
y_pred=svc_linear.predict(test_data)
cnf_matrix= confusion_matrix(test_label, y_pred)
print(cnf_matrix)
ac2=metrics.accuracy_score(test_label,y_pred)
acc2=ac2*100
print(acc2)

#rbf kernel
svc_linear=svm.SVC(kernel ="rbf", C=1)
svc_linear.fit(train_data,train_label)
y_pred=svc_linear.predict(test_data)
cnf_matrix= confusion_matrix(test_label, y_pred)
print(cnf_matrix)
ac3=metrics.accuracy_score(test_label,y_pred)
acc3=ac3*100
print(acc3)


'''y=[acc1,acc2,acc3]
x=["linear", "poly","rbf"]
pt.title("Kernel type v/s Accuracy")
pt.xlabel("Kernel type")
pt.ylabel("Accuracy")
pt.bar(x,y)
pt.show()
'''