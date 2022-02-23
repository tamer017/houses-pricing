import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("house-data.csv")
# remove the columns that will not affect our calculations 
# drop columns
#                              cleaning 
data=data.drop(["date","street","statezip","country","city"],axis=1)
float_data=data.select_dtypes(include="float")
# floor the values of the columns that should be int but it is float like the numer of rooms
for column in float_data.columns[1:]:
    float_data[column]=float_data[column].apply(np.floor)
int_data=data.select_dtypes(include="int")
# concate the int data and float data
data=pd.concat([float_data,int_data],axis=1)
c=data.corr()
sns.heatmap(c,annot=True)
plt.show()
