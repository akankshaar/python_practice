# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:40:12 2019

@author: Rhea Arora
"""

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
X=iris.data
y=iris.target
print(X)
print(y)

#split the data into training and testing
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.20)
gnb=GaussianNB()
mnb=MultinomialNB()
y_pred_gnb=gnb.fit(X_train, y_train).predict(X_test)
cnf_matrix_gnb=confusion_matrix(y_test, y_pred_gnb)
print(cnf_matrix_gnb)

y_pred_mnb=mnb.fit(X_train,y_train).predict(X_test)
cnf_matrix_mnb=confusion_matrix(y_test, y_pred_mnb)
print(cnf_matrix_mnb)

