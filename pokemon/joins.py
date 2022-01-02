# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:12:54 2019

@author: Rhea Arora
"""

#Joins

import pandas as pd
import numpy as np

dfRight = pd.DataFrame({"e_id":[10,20,30,40,50], "e_name":["Ram","Chintu","Pintu","Sam","Glam"],"e_ad":["Delhi","Punjab","UP","Haryana","UK"],"mobile":[1,2,7,4,5]})
print(dfRight)

dfLeft = pd.DataFrame({"e_id":[10,20,30,40,50], "salary":[1000,2000,3000,4000,5000], "e_dep":["CS","IT","Biotech","Mechanical","Management"],"mobile":[1,2,8,4,5]})
print(dfLeft)
dfMerge = pd.merge(dfRight, dfLeft, on =["e_id","mobile"], how= "inner")
print(dfMerge)
dfRMerge = pd.merge(dfRight, dfLeft, on =["e_id","mobile"], how= "right")
print(dfRMerge)
dfLMerge = pd.merge(dfRight, dfLeft, on =["e_id","mobile"], how= "left")
print(dfLMerge)
dfOMerge = pd.merge(dfRight, dfLeft, on =["e_id","mobile"], how= "outer")
print(dfOMerge)
