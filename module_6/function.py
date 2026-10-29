#no parameter, no return function
def name():    
    print ("wali")

#call a function
name()

#parameterized function
def name(name):
    print(f"hello {name}")

name("Wali")

#default parameter
def name(user = "you did not enter a name"):
    print(f"hello {user}")
name()

