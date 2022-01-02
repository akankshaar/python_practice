# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:50:54 2019

@author: Rhea Arora
"""

from tkinter import *
master = Tk()
w=Scale(master, from_=0, to=42)
w.pack()
w=Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()
