import pandas as pd
import pandas as pd 
df = pd.read_csv('student_data.csv')
# print(df)
print(type(df))

student_id = df['StudentID']
# print(student_id)
print(type(student_id))

# csv file 
csv_data = pd.read_csv('student_data.csv')
print(csv_data)

#excel file 
excel_file = pd.read_excel('phitron_student_marks.xlsx')
# print(excel_file)
print(type(excel_file))

#parquet file 
parquet_file = pd.read_parquet('students.parquet')
# print(parquet_file)
print(type(parquet_file))

#json file 
json_file = pd.read_json('data.json')
print(json_file)
print(type(json_file))

