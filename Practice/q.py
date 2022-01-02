# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:32:59 2019

@author: Rhea Arora
"""

integer=int(input("enter an integer"))
sum=0
product=1
for i in range(integer):
    quit=input("Do you want to quit? If yes, press q ")
    if quit=="q":
        print("Sum is ",sum+integer)
        print("Product is ",product*integer )
        break
    else:
        print("Enter q to quit")