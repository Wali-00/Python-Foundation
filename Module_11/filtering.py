import pandas as pd
df = pd.read_csv('student_data.csv')

# filtering 
complete = df.loc[df['Location']=='Dhaka']