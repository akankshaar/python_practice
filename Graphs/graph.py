# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:25:15 2019

@author: Rhea Arora
"""

import matplotlib.pyplot as pt
import numpy as np
x=[1000,2000,3000,4000]
y=[2,3,4,5]
pt.title("House prices in Delhi")
pt.xlabel("House prices")
pt.ylabel("House size")
pt.plot(x,y,"r")
pt.plot(x,y,".")
pt.show
pt.savefig("Defaultchart.png", format="png")