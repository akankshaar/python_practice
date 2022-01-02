# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:47:26 2019

@author: Rhea Arora
"""

import numpy as np
import pandas as pd

#sort by index
arr=np.random.random((5,5))
df=pd.DataFrame(arr, index=[10,20,30,40,5])
print(df)

dfsorted=df.sort_index()
print("Sorted dataframe by index is ",dfsorted)
df=pd.DataFrame(arr, index=[10,20,30,40,5],columns=[5,1,3,2,4])
dfsortedC=df.sort_index(axis=1)
print(dfsortedC)

#Sort by value, by rows
dfVsorted=df.sort_values(20,axis=1)
print(dfVsorted)

#sort by value, by default= column
dfVCsorted=df.sort_values(3)
print(dfVCsorted)