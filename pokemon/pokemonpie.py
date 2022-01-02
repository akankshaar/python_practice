# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:40:31 2019

@author: Rhea Arora
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

df= pd.read_csv('C:\\Users\\Rhea Arora\\Documents\\python\\pokemon\\pokemon.csv', sep=',', skipinitialspace=True)

for i in df["Type 1"]:
    pt.pie(df)
    pt.show()