# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:48:49 2019

@author: Rhea Arora
"""

from tkinter import *
master=Tk()
w= Spinbox(master, from_=0, to=10, textvariable=var, value=9)
w.pack()

mainloop()