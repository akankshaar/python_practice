# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:23:51 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
root.geometry("400x400")
var=tk.IntVar()
uframe=tk.Frame(root)
dframe=tk.Frame(root)
rframe=tk.Frame(root)
b=tk.Button(uframe, text="Button 1",bg="#ff6677")
b.pack(side="left")
b1=tk.Button(uframe, text="Button 2",bg="#ff6677")
b1.pack(side="left")
b2=tk.Button(uframe, text="Button 3",bg="#ff6677")
b2.pack(side="left")
b3=tk.Button(dframe, text="Button 4",bg="#ff6677")
b3.pack()
rb1=tk.Radiobutton(rframe, text="Clothes", variable=var,value=1)
rb1.pack(side="bottom")
rb2=tk.Radiobutton(rframe, text="Mobiles", variable=var,value=2)
rb2.pack(side="bottom")
rb3=tk.Radiobutton(rframe, text="Shoes", variable=var,value=3)
rb3.pack(side="bottom")
uframe.pack(side="top")
dframe.pack(side="bottom")
rframe.pack(side="left")
root.mainloop()