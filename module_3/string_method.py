#find() use for finding index number of a sub-string

string = "Hey Wali, how are you? Wali"

# lower() use for lowercase string
lower_case = string.lower()
print(lower_case)

# upper() use for uppercase string
upper_case = string.upper()
print(upper_case)

# for searching we use 'in stringVariable'
# it return true or false 
print("wali" in lower_case)

# len() for string length
print(len(string))

# rfind() for find index number of sub-string from end
index1 = lower_case.rfind("wali")
print(index1)

# count() for count sub-string
count = lower_case.count("wali")
print(count)

# replace() for replace a sub-string
replace = string.replace("Wali","Wali Ullah")
print(replace)
