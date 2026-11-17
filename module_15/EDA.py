import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_data_updated.csv')
#Univariate analysis for categorical value
print(df.shape)#show the row and column

print(df.shape[0])#row
print(df.shape[1])#column

print(df.head(10))#first 10 row

print(df.sample(10))#random 10 row

print(df.describe())#show the statistical value of  numerical column

df.isnull()#show the null value with true false

print(df.isnull().sum())#show the null value of each column

print(df.duplicated())
df.drop_duplicates(inplace=True)#remove the duplicates value from main file

plt.title("Survival rate")
sns.countplot(data= df, x=df['Survived'])
plt.show()

(df['Survived'].value_counts()/len(df))*100 #percentage of survival


survival_count = df['Survived'].value_counts()
survival_label = df['Survived'].unique()
plt.pie(survival_count,autopct="%5.1F",labels=survival_label)
plt.title('Pie chart of survival rate')
plt.show()

#univariate value for numerical value
sns.histplot(df['Age'],bins= 50)
plt.show()


sns.kdeplot(df['Fare'])
plt.show()