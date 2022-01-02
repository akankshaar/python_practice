# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:37:38 2019

@author: Rhea Arora
"""

d={1:200,2:300,4:500}
print(d.keys())
k=input("Enter key to check if it exists")

if k in d.keys():
    print("Yes, the key exists!")
else: 
    print("It does not exist!")