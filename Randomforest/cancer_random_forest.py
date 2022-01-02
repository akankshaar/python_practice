# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 08:52:58 2019

@author: Rhea Arora
"""

from sklearn import metrics
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as pt
import numpy as np
from sklearn.ensemble import RandomForestClassifier

cancer=load_breast_cancer()
print(cancer)
X=cancer.data
y=cancer.target

print(X)
print(y)

X_train,X_test, y_train, y_test= train_test_split(X,y, test_size=0.20)

clf=RandomForestClassifier(n_jobs=2,random_state=0, criterion="entropy")
print(clf)

clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
ac1=metrics.accuracy_score(y_test,y_pred)
acc1=ac1*100
print(acc1)