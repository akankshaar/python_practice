# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:59:35 2019

@author: Rhea Arora
"""


import pandas as pd
import numpy as np
s=pd.Series([10,20,30,40])
print("Series from list is " ,s)
s1=pd.Series([10,20,30,40], index=['a','b','c','d'])
print('Series is ',s1)
s2=pd.Series([10,20,30,40], index=['a','b','c','d'], dtype= np.float32)
print("series is ", s2)
arr=np.arange(15,30,2)
s4=pd.Series(arr)
print("Series from array is ", s4)
d={'Delhi':200, 'Haryana':300,'UP':400}
s5=pd.Series(d)
print("Series from dictionary is ",d)

size=int(input("Input the size of dictionary"))
d={}
for i in range(size):
    key=input("Enter the key")
    value=input("Enter the value")
    size2=int(input("Input the size of the second dictionary"))
    d1={}
    for j in range(size2):
        key2=input("Enter the key for nested dictionary")
        value2=input("Enter the value for nested dictionary")
        d[key2]=value2
        
        
    