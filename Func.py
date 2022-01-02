# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:02:36 2019

@author: Rhea Arora
"""
#vargs
def PrintData(*V):
    for x in V:
        print(x)
        
PrintData(10,20,30)                  
PrintData(1,2,3,4,5)

#keyvargs
def PrintData(**k):
    print(k)
    
PrintData(a=10,b=20,c=30)

import numpy as np
arr=np.array([1,2,3,4])
arr
type(arr)
arr/2
arr*2
arr.shape
arr.ndim #gives dimension
arr=np.array([[1,2,3],[4,5,6]])
arr.shape
arr.ndim

