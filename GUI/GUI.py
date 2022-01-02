# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:08:57 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
var=tk.IntVar()
def getData():
    v=var.get()
    print("Value is " , v)
rm=tk.Radiobutton(root,variable=var,text="Male", value=1).grid(row=0, column=0)
rf=tk.Radiobutton(root,variable=var,text="Female", value=2).grid(row=0, column=1)
b=tk.Button(root, text="Click", command=getData).grid(row=2, column=1)
root.mainloop()