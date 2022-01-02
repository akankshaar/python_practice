# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:10:42 2019

@author: Rhea Arora
"""

kevin_score=0
stuart_score=0
V=["a","e","i","o","u"]
s=input("Enter a string")

for i in range(len(s)):
    if s[i] in V:
        kevin_score=kevin_score+1
        print(kevin_score)
    else:
        stuart_score=stuart_score+1
        
    if kevin_score>stuart_score:
        print("Kevin won")
    elif kevin_score<stuart_score:
        print("Stuart won")
    else:
        print("It's a tie!")
    