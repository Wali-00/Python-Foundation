import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_data_updated.csv')

sns.countplot(data=df , x=df['Sex'], hue= df['Survived'])
sns.countplot(x=df['Pclass'],hue=df['Survived'])

