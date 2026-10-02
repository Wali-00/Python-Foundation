# index of a string
string = "wali ullah"
print(string[5])

message = """hey wali how are you?
i'm great 
how about u? i hear that you are learning AI/ML?
yeap thats true...
"""

# slice 
first_message = message[0:20]
print(first_message)

# print from reverse
print(first_message[-1])
print(first_message[-2])
print(first_message[-3])

# find index number of sub-string from starting
lower_case= first_message.lower() #lower() use for lower case
index = lower_case.find("wali")
print(index)

