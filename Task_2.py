import pandas as pd
import numpy as np
from scipy import stats
import warnings



df=pd.read_csv("D:/Data Analytics/Techno_Hacks/Task_2.csv")
#print(df.count())
df=df.dropna()
#print(df.count())
x=df['Age']
print("For Age:")
a=np.mean(x)
print("Mean",a)
b=np.median(x)
print("Median",b)
c=np.std(x)
print("Standard Deviation",c)
d=stats.mode(x)
print("Mode:",d.mode[0])

y=df['Fare']
print("For Fare:")
am=np.mean(y)
print("Mean",am)
bm=np.median(y)
print("Median",bm)
cm=np.std(y)
print("Standard Deviation",cm)
dm=stats.mode(y)
print("Mode",dm.mode[0])