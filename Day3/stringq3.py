# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:25:28 2019

@author: Rhea Arora
"""

l=['abc', 'xyz', 'aba', '1221']

count=0

for i in l:
    if i[1]==i[-1] and len(i)>2:
        count=count+1
        
print("count = ",count)