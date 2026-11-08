import pandas as pd
df = pd.read_csv('student_data.csv')
#value change 
df.loc[1,'Python Marks']=90
df.head(3)


#itteration 
for i, series in df.iterrows():
    print(f"{i} : {series}")

for i in df.itertuples(index = False):
    print(i)