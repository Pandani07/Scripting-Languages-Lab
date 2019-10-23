import pandas as pd
import numpy as np

datad=pd.read_csv("StudentsPerformance.csv")

#1
print(datad.head())

#2
datad.drop(['test preparation course','lunch'],  axis=1,inplace=False)
print(datad)

#3
datad['parental level of education']=datad['parental level of education'].fillna('Basic level of education')
print(datad)

#4
datad["race/ethnicity"]=datad["race/ethnicity"].map({
    "group A":"Asian Students",
    "group B":"African Students",
    "group C":"Afro-Asian Students",
    "group D":"American Students",
    "group E":"European Students"
})


datad["test preparation course"]=datad["test preparation course"].map({
    "none":0,
    "completed":1
})
#print(datad)
datad=datad.rename(columns={'reading score':'readscore','writing score':'writescore'}, inplace=False)

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sn
ax=sn.countplot(x="test preparation course", hue="gender", palette="Set3", data=datad)
plt.show()

bx=sn.countplot(x="race/ethnicity",hue="gender",palette="Set2", data=datad)
plt.show()

interval=[0,40,60,75,100]
categories=['Fail','Second class','First Class','Distinction']
datad["Total MMarks"]=pd.cut(datad.mathscore, interval, labels=categories)
ax=sn.countplot(x='Total MMarks',hue='gender',palette='Set1',data=datad).set(title="Math score plot",xlabel="Classes",ylabel="Number of students")
plt.show()

interval=[0,40,60,75,100]
categories=['Fail','Second class','First Class','Distinction']
datad["Total RMarks"]=pd.cut(datad.readscore, interval, labels=categories)
ax=sn.countplot(x='Total RMarks',hue='gender',palette='Set1',data=datad).set(title="Reading score plot",xlabel="Classes",ylabel="Number of students")
plt.show()

interval=[0,40,60,75,100]
categories=['Fail','Second class','First Class','Distinction']
datad["Total WMarks"]=pd.cut(datad.writescore, interval, labels=categories)
ax=sn.countplot(x='Total WMarks',hue='gender',palette='Set1',data=datad).set(title="Writing score plot",xlabel="Classes",ylabel="Number of students")
plt.show()
