#open and read a file
file = open("./module_7/read.txt","r")
#print(file.read())
#if we dont have the file which we give in the location it will shown a error

#content = file.read()
#print(type(content)) string
#print(content) hello wali

content = file.readlines()
print(type(content))#list
print(content)#[hello wali\n, how are u]

#if we want to remove the \n
#also remove the first and last unnecessary space
content = list(map(str.strip,content))
print(content)

# here we need to close the file manually
print(file.closed)#false
file.close()
print(file.closed)