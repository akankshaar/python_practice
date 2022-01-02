# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:35:05 2019

@author: Rhea Arora
"""

import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

x=np.random.randn(4,4)
df=pd.DataFrame(x,index=[2001,2002,2003,2004])
print(df)
pt.hist(df)
pt.show()