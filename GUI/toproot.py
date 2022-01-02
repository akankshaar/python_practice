# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:38:15 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
def top():
    toproot=tk.Toplevel()
    toproot.title("Window 2")
    b1=tk.Button(toproot, text="button 1")
    b1.pack()
    
root.title("Window 1")
b=tk.Button(root, text="Button 1", command=top)
b.pack()
root.mainloop()
