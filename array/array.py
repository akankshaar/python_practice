# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:43:26 2019

@author: Rhea Arora
"""

import numpy as np

#we can also use asarray to create arrays the only difference is between the number of arguments
arr=np.array([1,2,3,4])
print(arr)
ar=np.arange(10)
print(ar)
ar= np.arange(5,10,2)
print(ar)
arr=np.asarray([1,2,3,4], dtype=np.float32)
print(arr.itemsize)
arr=np.asarray([1,2,3,4], dtype=np.float64)
print(arr.itemsize)
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
arr=np.resize(arr,(7,7))
print(arr)
arr=np.resize(arr,(2,4))
print(arr)
x=np.full((2,4),7)
print(x)
r=np.random.random((3,3))
print(r)
xr=np.append(x,r) #include axis if you dont want 1-D array
print(xr)
xrshape=xr.shape
print(xrshape)
arr=np.array([[1,2,3,4],[5,6,7,8]])
np.savetxt("myfile.txt",arr)
print("file saved")
#different location file also
data=np.loadtxt("myfile.txt",skiprows=1) #skip rows skips the first row
print(data)
np.insert()
