import numpy as np
import pandas as pd
from sklearn import tree
import re

data = pd.read_csv("titanic.csv",usecols=["Pclass","Fare","Age","Sex","Survived"])
data = data[data['Age'].notnull()]

data['Sex'][data['Sex']=='female']=0
data['Sex'][data['Sex']=='male']=1
# print (data)


clf = tree.DecisionTreeClassifier(random_state=241)
survivers = list(data["Survived"])
data = data[['Pclass','Fare','Age','Sex']]


X = np.array(data)
Y = np.array(survivers)
clf=clf.fit(X,Y)
print(clf.feature_importances_)


# X = data
# X=[[1,2],[3,4],[5,6],[7,8],[9,0]]
# Y=[2,4,6,8,0]?
# clf = clf.fit(X,Y)
# dotfile = open('/Users/woqpw/github/datascience/tree.dot','w')
# dotfile = tree.export_graphviz(clf, out_file = dotfilew)
# dotfile.close()
# print (pd.DataFrame(clf.feature_importances_,columns=['Imp']))
# print(clf.feature_importances_)
# print(data)
# print("___________")
# print(Y)
