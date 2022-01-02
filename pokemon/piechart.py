# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:04:53 2019

@author: Rhea Arora
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

df=pd.read_csv("C:\\Users\\Rhea Arora\\Documents\\python\\pokemon\\pokemon.csv")
maxm= df["Attack"][0]
for i in range(800):
    if df["Attack"][i]>maxm:
        maxm=df["Attack"][i]
        x=df.iloc[i:i+1,6:11]
        pt.title(df["Name"][i])
l=[]

for i in df.columns:
    l.append(i)
labelp=[]
for i in range(6,11):
    labelp.append(l[i])
pt.pie(x, labels=labelp)
pt.show()
