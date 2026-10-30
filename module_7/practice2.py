#read and write in the same file
with open("./module_7/practice2.txt","w+")as file:
    file.write("Hello Wali")
    print(file.tell())#10
    file.seek(0)
    print(file.tell())#0
    print(file.read())
    file.truncate(5)#remove data from index 5
    file.seek(0)
    print(file.read())
