# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:13:22 2019

@author: Rhea Arora
"""

s="BANANA"

length=len(s)
l=[]    
for i in range(length):
    for j in range(i,length):
        l.append(s[i:j+1])
print(l)

    
        