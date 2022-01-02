# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:44:14 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
l=tk.Listbox(root)
l.insert(1,'c')
l.insert(2,'c++')
l.insert(3,'python')
l.pack()

root.mainloop()