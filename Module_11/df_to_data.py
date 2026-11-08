import pandas as pd
df = pd.read_csv('student_data.csv')

#transforming to df from inbuilt datas 
my_list =[["wali",90],["israt",90],["tanvir",90],["onik",90]]
data = pd.DataFrame(my_list,columns=['Names','Marks'],index=['i','ii','iii','iv'])
print(type(data))
print(data)

#dictionary
my_dict = {
    'Name':["wali","rony","rasel","reza"],
    'Age':[23,26,30,29]
}

my_data = pd.DataFrame(my_dict)
print(my_data)

my_dic = [
    {"name":'wali','age':23,'mark':90},
    {"name":'israt'}
]
my_data = pd.DataFrame(my_dic)
print(my_data)