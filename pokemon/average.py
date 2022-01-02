# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 08:39:46 2019

@author: Rhea Arora
"""

import pandas as pd
import numpy as np

df=pd.read_csv("C:\\Users\\Rhea Arora\\Documents\\python\\pokemon.csv")
sums=0
count=0
arr=np.array([[],[]])
l=[]

for i in range(800):
    if df["Type 1"][i]=="Grass":
    df1=df.iloc[1:1+1,:]
    arr