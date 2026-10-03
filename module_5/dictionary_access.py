dic = {"name":"wali", "age":23, "address":"Dhaka","numbers":[10,20,30]}

print(dic["name"])
print(dic.get("numbers"))

# assign vale 
dic["name"] = "wali ullah"
print(dic.get("name"))

#if a value not in dictionary it will show none or we can show something by ourself
print(dic.get("math_numbers")) #none
print(dic.get("math_numbers",00))  #0
