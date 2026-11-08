import pandas as pd
df = pd.read_csv('student_data.csv')

copy = df.sort_values('Data Structure Marks')#acending 
copy = df.sort_values(['Python Marks'],ascending=False)#descending
copy = df.sort_values(['Python Marks','Data Structure Marks'],ascending=False)#first tar value soman hle next ta dekhbe
copy = df.sort_values(['Python Marks','Data Structure Marks'],ascending=[0,1])#first ta des krlew prer ta ac e krbe

