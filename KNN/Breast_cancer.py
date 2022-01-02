# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:03:50 2019

@author: Rhea Arora
"""

from sklearn import svm, metrics
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as pt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

cancer=load_breast_cancer()
print(cancer)
X=cancer.data
y=cancer.target

print(X)
print(y)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.20)

#Applying KNN
classifier= KNeighborsClassifier(n_neighbors=5)
print(classifier)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
ac1=metrics.accuracy_score(y_test,y_pred)
acc1=ac1*100
print(acc1)

#Applying SVM

svc_linear=svm.SVC(kernel ="linear", C=1)
svc_linear.fit(X_train,y_train)
y_pred=svc_linear.predict(X_test)
cnf_matrix= confusion_matrix(y_test, y_pred)
print(cnf_matrix)
ac2=metrics.accuracy_score(y_test,y_pred)
acc2=ac2*100
print(acc2)

#Making graph
y=[acc1,acc2]
x=["KNN", "SVM"]
pt.title("Accuracy in KNN and SVM")
pt.xlabel("Classifier type")
pt.ylabel("Accuracy")
pt.bar(x,y)
pt.show()