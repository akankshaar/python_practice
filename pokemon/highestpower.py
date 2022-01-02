# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 08:49:57 2019

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
        x=df.iloc[i:i+1,:]
print("Pokemon with the highest power = ", maxm)
print(x)

maxm=np.asarray(maxm)
maxm.shape=(-1,1)
pt.pie(maxm)
pt.show()
pt.axis("equal")