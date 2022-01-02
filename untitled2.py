# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:03:16 2019

@author: Rhea Arora
"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
from sklearn import svm, metrics
from sklearn.metrics import confusion_matrix
import os
import glob
import cv2
import numpy as np
import matplotlib.image as mimg
import matplotlib.pyplot as pt

paths=[]
samp=0
count=-1
for i in range (1,samp+1):
    #plt.cla() #to clear axis    count=count+1
    print(count)
    path="C:\\Users\\Rhea Arora\\Documents\\python\\brain_tumor\\new_train\\d(%d).png"
    paths.append(path)
np.random.shuffle(paths)
for i in paths:
  count=count+1
  im=mimg.imread(i)
  im_r=im
  im_r=cv2.resize(im_r,(64,64))
  im_r.reshape(1,64,64)