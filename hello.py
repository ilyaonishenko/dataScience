import pandas
import numpy as np
import re
from collections import defaultdict

# 1 tast
data = pandas.read_csv("titanic.csv")
female_number=0;
male_number=0;
sexArray = list(data.get("Sex"))
for i in sexArray:
	if i == 'female':
		female_number+=1
	if i=="male":
		male_number+=1
#891
print ("female: ",female_number," male: ",male_number)
# 2 task
# print(data)
survivesList = list(data.get("Survived"))
N = len(survivesList)
# print(N)
survives = 0
for man in survivesList:
	if man ==1:
		survives+=1
print("survives ",(survives/N)*100)
#3 task
firstClassList = list(data.get("Pclass"))
firstclass =0
for man in firstClassList:
	if man==1:
		firstclass+=1
print("firstclass ",(firstclass/N)*100)
#4 task
testArray = ([1,2,3,4,5])
ageList = np.array(data.get("Age"))
# print(ageList)
median = np.nanmedian(ageList) # медиана
mean = np.nanmean(ageList)# среднее
# print(testArray)
# print(len(testArray),len(ageList))
# print(np.mean(testArray))
# print(np.median(testArray))
print("median ",median," mean ",mean)
#5 task
sibsp = np.array(data.get("SibSp"))
parch = np.array(data.get("Parch"))
print("pearson: ",np.corrcoef(sibsp,parch)[0,1])
#6 task
female_data = data[['Name','Sex']][data[['Name','Sex']]['Sex']=="female"]
# female_data = [data['Sex']=="female"][['Name','Sex']]
namesList = np.array(female_data['Name'])
# print(female_data)

def noBrackets(str):
	pattern = re.compile(r'Miss\. (\w+)')
	return "".join(pattern.findall(str))
#если есть скобки.
def openBrackets(str):
	pattern = re.compile(r'\((\w+)')
	inbrackets = "".join(pattern.findall(str))
	return inbrackets
# print(namesList)
# namesList2 = namesList[:10]
# print(noBrackets(namesList2[1]))
# print(namesList2)
counter = defaultdict(int)
for str in namesList:
	if re.findall('\(',str)!='None':
		newStr = openBrackets(str)
		counter[newStr]+=1
	if re.findall(r'Miss\S',str)!='None':
		counter[noBrackets(str)]+=1
print(counter)
