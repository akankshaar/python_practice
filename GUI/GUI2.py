# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:59:16 2019

@author: Rhea Arora
"""

from tkinter import *

master=Tk()
variable=StringVar(master)
variable.set("one")
l=Label(master, text="State").grid(row=0)
l1=Label(master, text="City").grid(row=1)
w=OptionMenu(master, variable, "UP","MP","Punjab").grid(row=0, column=1)
w1=OptionMenu(master, variable, "Haridwar","Patna","Amr").grid(row=0, column=1)
