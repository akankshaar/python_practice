# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:50:58 2019

@author: Rhea Arora
"""


import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\Rhea Arora\\Documents\\python\\pokemon\\pokemon.csv")
user=input("Enter the name of the pokemon")
for i in range(800):
    if df["Name"][i] == user:
       x=df.iloc[i:i+1,6:12]
       
print(x)
pt.hist(x)
pt.show()