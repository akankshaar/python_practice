# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:57:56 2019

@author: Rhea Arora
"""

import tkinter as tk
root=tk.Tk()
def click():
    i=0
    toproot=tk.Toplevel(root)
    global e1
    e1=tk.Entry(toproot)
    e1.pack()
    b1=tk.Button(toproot, text="enter name", command=getUsername)
    b1.pack()
    global e2
    e2=tk.Entry(toproot)
    e2.pack()
    b2=tk.Button(toproot, text="Enter password", command=getPassword)
    b2.pack()
    i=i+1
def getUsername():
    if e1.get()=="admin":
        print(e1.get())
    else:
        print("User invalid")
def getPassword():
    print(e2.get())
    if e2.get()=="1234":
        print(e2.get())
    else:
        print("User invalid")
root.title("My window 1");
root.geometry("300x100") #not multipy sign, ex "x"
b=tk.Button(root, text="Click",command=click,bg='#ff8899',fg='Red',width=5,height=5,activeforeground='Blue',activebackground='#ff0099')
b.pack()           
root.mainloop()
