# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:40:06 2019

@author: Twinkle
"""

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
iris=datasets.load_iris()
x=iris.data
y=iris.target
print(x)
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
gnb=GaussianNB()
mnb=MultinomialNB()
y_pred_gnb=gnb.fit(x_train,y_train).predict(x_test)
print(metrics.accuracy_score(y_test,y_pred_gnb))

y_pred_mnb=mnb.fit(x_train,y_train).predict(x_test)
print(metrics.accuracy_score(y_test,y_pred_mnb))