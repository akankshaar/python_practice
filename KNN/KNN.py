# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:42:49 2019

@author: Rhea Arora
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import metrics,datasets
import matplotlib.pyplot as pt
import numpy as np

iris=datasets.load_iris()
print(iris)
X=iris.data
y=iris.target

print(X)
print(y)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.20)
print("train x",X_train.shape)
print("test x",X_test.shape)
print("train y",y_train.shape)
print("test y",y_test.shape)

classifier= KNeighborsClassifier(n_neighbors=5)
print(classifier)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
acc1=metrics.accuracy_score(y_test,y_pred)
print(acc1)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.30)
print("train x",X_train.shape)
print("test x",X_test.shape)
print("train y",y_train.shape)
print("test y",y_test.shape)

classifier= KNeighborsClassifier(n_neighbors=5)
print(classifier)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
acc2=metrics.accuracy_score(y_test,y_pred)
print(acc2)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.40)
print("train x",X_train.shape)
print("test x",X_test.shape)
print("train y",y_train.shape)
print("test y",y_test.shape)

classifier= KNeighborsClassifier(n_neighbors=5)
print(classifier)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
acc3=metrics.accuracy_score(y_test,y_pred)
print(acc3)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.15)
print("train x",X_train.shape)
print("test x",X_test.shape)
print("train y",y_train.shape)
print("test y",y_test.shape)

classifier= KNeighborsClassifier(n_neighbors=5)
print(classifier)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
acc4=metrics.accuracy_score(y_test,y_pred)
print(acc4)

df=[acc4,acc1,acc2,acc3]
print(df)
x=df
y=[0.15,0.20,0.30,0.40]
pt.title("Accuracy v/s test size")
pt.xlabel("Accuracy")
pt.ylabel("Test size")
pt.bar(x,y)
pt.show()