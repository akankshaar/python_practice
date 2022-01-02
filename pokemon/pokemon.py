# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:24:45 2019

@author: Rhea Arora
"""

import numpy as np
import pandas as pd

df= pd.read_csv("C:\\Users\\Rhea Arora\\Documents\\python\\pokemon.csv")
print(df)
       
g=df.groupby("Type 1")
print(g)

'''grass=g.get_group("Grass")
print(grass)

fire=g.get_group("Fire")
print(fire)'''