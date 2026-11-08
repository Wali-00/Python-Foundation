import pandas as pd
df = pd.read_csv('student_data.csv')

#data accessing with loc 
df.loc[0]#0 no row, all col 
df.loc[[2,3,5]] #2,3,5 row, all col 
df.loc[3:7]#3-7 row
df.loc[2:4,'Python Marks']#row and columns

df_index = df.set_index('StudentID')# feature name wise manage kre dite hbe
df.rename(columns={'FullName':'Full Name'})

#Dropping rows and columns,Assigning values and Iteration
#row deletion
# df.drop(0, inplace=True)
#column deletion 
# df.drop('CompletionStatus',axis=1,inplace=True)

