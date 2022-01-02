# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:54:58 2019

@author: Rhea Arora
"""

#pokemon fight

import numpy as np
import pandas as pd

xp=0
cp=0
df=pd.read_csv("C:\\Users\\Rhea Arora\\Documents\\python\\pokemon\\pokemon.csv")
user=input("Enter the name of the pokemon")
for i in range(800):
    if df["Name"][i] == user:
       x=df.iloc[i:i+1,:]
       #in iloc= i+1 excluded, loc= i+1 included
comp=df.sample()
print("User chose : ",x)
print("Computer chose : ",comp)
xa=np.array([])
ca=np.array([])

for i in range(6,11):
    xa=np.append(xa,x.iloc[:,i:i+1])
    ca=np.append(ca,comp.iloc[:,i:i+1])
for i in range(5):
    if xa[i]>ca[i]:
        xp=xp+1
    else:
        cp=cp+1
        
if xp>cp:
    print("User won!")
elif cp>xp:
    print("Computer won!")
else:
    print("It's a tie!")

    