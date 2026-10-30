# write mode creates a new file if it does not exist or truncates the file if it exists

with open("./module_7/write.txt","w") as file:
    file.write("Hello wali\n")
    file.write("How is learning going on?")

#if we again write on the same file it overwrites the file

with open("./module_7/write.txt","w")as file:
    file.write("Hey\n")
    
    file.write("How is learning going on?\n")

#append mode

with open("./module_7/write.txt","a")as file:
    file.write("The learning of AI/ML is fun\n")
    file.write("I am enjoying the classes\n")

strings =["Apple","Banana","Orange"]
with open("./module_7/write.txt","a")as file:
    file.writelines(strings)