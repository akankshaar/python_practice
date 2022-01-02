# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:21:00 2019

@author: Rhea Arora
"""

from sklearn import linear_model

features=[[2],[1],[5],[10]]
labels=[27,11,75,155]

clf=linear_model.LinearRegression()
print(clf)
clf=clf.fit(features, labels)

predicted= clf.predict([[9]])
print(predicted)
