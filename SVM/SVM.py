# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:01:15 2019

@author: Rhea Arora
"""

from sklearn import svm, metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as pt
import numpy as np
from sklearn.model_selection import train_test_split

iris=load_iris()
x=iris.data
y=iris.target
#Split data into test and train
X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.3)

#Linear kernel
svc_linear=svm.SVC(kernel ="linear", C=1)
svc_linear.fit(X_train,y_train)
y_pred=svc_linear.predict(X_test)
cnf_matrix= confusion_matrix(y_test, y_pred)
print(cnf_matrix)
ac1=metrics.accuracy_score(y_test,y_pred)
acc1=ac1*100
print(acc1)

#Poly kernel
svc_linear=svm.SVC(kernel ="poly", C=1)
svc_linear.fit(X_train,y_train)
y_pred=svc_linear.predict(X_test)
cnf_matrix= confusion_matrix(y_test, y_pred)
print(cnf_matrix)
ac2=metrics.accuracy_score(y_test,y_pred)
acc2=ac2*100
print(acc2)

#rbf kernel
svc_linear=svm.SVC(kernel ="rbf", C=1)
svc_linear.fit(X_train,y_train)
y_pred=svc_linear.predict(X_test)
cnf_matrix= confusion_matrix(y_test, y_pred)
print(cnf_matrix)
ac3=metrics.accuracy_score(y_test,y_pred)
acc3=ac3*100
print(acc3)

y=[acc1,acc2,acc3]
x=["linear", "poly","rbf"]
pt.title("Kernel type v/s Accuracy")
pt.xlabel("Kernel type")
pt.ylabel("Accuracy")
pt.bar(x,y)
pt.show()
