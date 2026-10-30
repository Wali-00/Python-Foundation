with open("./module_7/pointer.txt","r")as file:
    #tell()point the cursor initially in 0 no index
    print(file.tell())#0
    print(file.read())
    print(file.tell())#last
    print(file.read())#read nothing

with open("./module_7/pointer2.txt","w")as file:
    file.write("Hello World")

with open("./module_7/pointer2.txt","r")as file:
    print(file.tell())#0
    print(file.read(5))#Hello
    print(file.tell())#5
    print(file.read())#World
    print(file.tell())#11


with open("./module_7/pointer2.txt","r")as file:
    print(file.tell())#0
    file.seek(5)#5
    print(file.tell())#5

