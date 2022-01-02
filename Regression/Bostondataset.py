# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:53:29 2019

@author: Rhea Arora
"""

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_boston
from sklearn import metrics,datasets
import matplotlib.pyplot as pt
import pandas as pd
from sklearn import linear_model

boston=datasets.load_boston()
print(boston)
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)
bos=pd.DataFrame(boston.data)
print(bos)
bos.columns=boston.feature_names
print(bos)

bos["PRICE"]=boston.target
Square_feets=bos["ZN"]
Square_feets=np.asarray(Square_feets)
Square_feets.shape=(-1,1)

clf=linear_model.LinearRegression()
print(clf)
clf=clf.fit(Square_feets,boston.target)

y_pred= clf.predict([[2000]])
print(y_pred)
