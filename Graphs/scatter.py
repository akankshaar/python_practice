# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:14:52 2019

@author: Rhea Arora
"""

import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

pt.plot([1,2,3,4],[10,20,30,40], color="lightblue", linewidth="3")
pt.scatter([0.3,3.8,1.2,2.5],[11,25,9,26], color="darkgreen", marker="*")
pt.xlim(0.5,4.5)
pt.show()
