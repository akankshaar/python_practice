"""
Created on Tue Jul  2 09:06:09 2019

@author: Rhea Arora
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

np.random.seed(0)

data=load_iris()
print(data)

df=pd.DataFrame(data.data, columns=data.feature_names)
print(df.head())

df["species"]=pd.Categorical.from_codes(data.target,data.target_names)
print(df)

df["is_train"]=np.random.uniform(0,1,len(df))<=0.75
print(df)

train_data, test_data= df[df["is_train"]==True], df[df["is_train"]==False]
print(train_data)

len(test_data)
features=df.columns[:4]
print(features)

y=pd.factorize(train_data["species"])[0]
print(y)

clf=RandomForestClassifier(n_jobs=2,random_state=0)
print(clf)

clf.fit(train_data[features],y)
clf.predict(test_data[features])

print(clf.predict_proba(test_data[features])[0:10])
print(clf.predict_proba(test_data[features])[10:20])

pred=data.target_names[clf.predict(test_data[features])]
print(pred)

print(test_data["species"].head())
print(pd.crosstab(test_data["species"],pred,rownames=["Actual Species"], colnames=["Predicted Species"]))
