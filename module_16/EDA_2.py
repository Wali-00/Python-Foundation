from ydata_profiling import ProfileReport
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

base_dir = Path(__file__).resolve().parent
titanic_df = pd.read_csv(base_dir / 'titanic_data_updated.csv')

sns.countplot(data=titanic_df, x='Sex', hue='Survived')
sns.countplot(data=titanic_df, x='Pclass', hue='Survived')

# proportion
age_survival = titanic_df.groupby('Age')['Survived'].value_counts(normalize=True)
print(age_survival)

sns.barplot(data=titanic_df, x='Pclass', y='Fare')
sns.barplot(data=titanic_df, x='Survived', y='Age', hue='Sex')
sns.barplot(data=titanic_df, x='Survived', y='Age')

# kde plot for categorical discrepancy
sns.kdeplot(data=titanic_df, x='Age', hue='Survived', common_norm=False)

# scatter plot
tips_df = sns.load_dataset('tips')
sns.scatterplot(data=tips_df, x='total_bill', y='tip', hue='sex', size='size')

plt.show()

profile = ProfileReport(titanic_df, title='Titanic Profile Report')
profile.to_file(base_dir / 'my_report.html')