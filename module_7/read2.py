with open("./module_7/read.txt","r") as file:
    #print(file.read())
    for line in file:
        print(line,end="")
        l = line.strip()

print(file.closed)

