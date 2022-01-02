# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:32:07 2019

@author: Rhea Arora
"""

from sklearn.datasets import load_digits
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

data=load_digits()
print(data)

print("Shape of target", data.target.shape)
print("Image data shape", data.data.shape)
plt.figure(figsize=(20,4))

#slicing
for index,(image, label) in enumerate(zip(data.data[0:5], data.target[0:5])):
    plt.subplot(1,5, index+1)
    plt.imshow(np.reshape(image,(8,8)), cmap=plt.cm.afmhot)
    plt.title("t % d" % label, fontsize=10)
    
x_train, x_test, y_train,y_test=train_test_split(data.data, data.target, test_size=0.23)
print(x_train.shape)
print(x_test.shape)

lr=LogisticRegression()
lr.fit(x_train,y_train)
#predicting 0 index
print(lr.predict(x_test[0].reshape(1,-1)))
#predicting 0 to 9
print(lr.predict(x_test[0:10]))

predictor=lr.predict(x_test)
score=lr.score(x_test, y_test)
print(score)

cm=metrics.confusion_matrix(y_test, predictor)
print(cm)

plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=" .3f", linewidth=.5, square=True)
plt.ylabel("Actual data")
plt.xlabel("Predicted data")
all_title="Accuracy {0}".format(score)
plt.title(all_title, size=15)

