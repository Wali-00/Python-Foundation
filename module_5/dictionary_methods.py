#we can add value with update methods
dic = {"name":"wali", "age":23, "address":"Dhaka","numbers":[10,20,30]}

dic.update({"math_numbers":95})
print(dic)

# pop() remove specific key
dic.pop("math_numbers")
print(dic)

# popitem() remove last key
dic.popitem()
print(dic)

# also can delete specific value with del
del dic["address"]
print(dic)

#we can copy dic 
dic2 = dic.copy()
print(dic2)
