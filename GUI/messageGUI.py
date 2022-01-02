# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:19:00 2019

@author: Rhea Arora
"""

from tkinter import *
main=Tk()
ourMessage= "This is our message"
messageVar= Message(main, text=ourMessage)
messageVar.config(bg="lightgreen") #when we have to modify something later we use config
messageVar.pack()
main.mainloop()