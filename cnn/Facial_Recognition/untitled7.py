# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:46:29 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
def click():
    i=0
    print("Hello")
    label=tk.Label(root, text="hello", fg="#ff0000")
    label.pack()
    toproot=tk.Toplevel(root)
    global e1
    e1=tk.Entry(toproot)
    e1.pack()
    b1=tk.Button(toproot, text="newbutton", command=getData)
    b1.pack()
    i=i+1
    
def getData():
    print(e1.get())
root.title("My window 1");
root.geometry("300x100") #not multipy sign, ex "x"
b=tk.Button(root, text="Click",command=click,bg='#ff8899',fg='Red',width=5,height=5,activeforeground='Blue',activebackground='#ff0099')
b.pack()           
root.mainloop()
