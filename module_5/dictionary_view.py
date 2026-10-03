dic = {"name":"wali", "age":23, "address":"Dhaka","numbers":[10,20,30]}

#keys(), values(), items() these are live methods

key = dic.keys()
print(key)
dic["math_numbers"]=95
print(key)

value = dic.values()
print(value)

item = dic.items()
print(item)

for key,value in dic.items():
    print(key,value)
    