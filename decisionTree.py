import numpy as np
import pandas as pd
from sklearn import tree
import re

data = pd.read_csv("titanic.csv",usecols=["Pclass","Fare","Age","Sex","Survived"])
data = data[data['Age'].notnull()]

data['Sex'][data['Sex']=='female']=0
data['Sex'][data['Sex']=='male']=1

clf = tree.DecisionTreeClassifier(random_state=241)
survivers = list(data["Survived"])
data = data[['Pclass','Fare','Age','Sex']]

X = np.array(data)
Y = np.array(survivers)
clf=clf.fit(X,Y)

print(clf.feature_importances_)
