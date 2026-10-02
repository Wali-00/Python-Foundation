# split
prom = "hey wali what are you doing man ?"
tokens = prom.split() # by default it split string with space
print(tokens)
print(type(prom)) #str
print(type(tokens)) #list

# split with parameter
prom1 = "hey-wali-what-are-you-doing-man ?" #we can use other sign also
tokens1 = prom1.split("-")
print(tokens1)

# join
tokens2 = "=".join(tokens)
print(tokens2)
print(type(tokens2)) # str

#formatting
name = "wali"
age = 23
height = 5.43

print(f"he is {name}. he is {age} years old. he is {height} feet tall")

# we can use methods with variable in formatted string
print(f"he is {name.upper()}. he is {height:.2} feet tall")

# we can store formatted string
model_accuracy = 0.8333
var = f"the model accuracy is {model_accuracy}"
var1 = f"the model accuracy is {model_accuracy:.2%}"
print(var)
print(var1)
print(type(var))
print(type(var1))
