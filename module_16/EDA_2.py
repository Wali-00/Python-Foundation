import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_data_updated.csv')

sns.countplot(data=df , x=df['Sex'], hue= df['Survived'])
sns.countplot(x=df['Pclass'],hue=df['Survived'])

#proportion 
gender_split = df.groupby('Age')['Survived'].value_counts(normalize=True)
print(gender_split)

sns.barplot(x=df['Pclass'],y=['Fare'])
sns.barplot(x=df['Survived'],y=df['Age'],hue=df['Sex'])
sns.barplot(x=df['Survived'],y=df['Age'])