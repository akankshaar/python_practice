# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:41:40 2019

@author: Rhea Arora
"""
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets, metrics, svm

X,y=datasets.load_iris(return_X_y=True)
print(X.shape)
print(y.shape)
train_data, test_data, train_label, test_label=train_test_split(X,y, test_size=0.2, random_state=1)
print(test_label)
model_svm=svm.SVC(kernel="linear")
val= cross_val_score(model_svm, train_data, train_label, cv=5)
print(val)
print(val.mean())