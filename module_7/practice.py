#total lines, total words in line, total character in lines

from functools import reduce
with open("./module_7/practice.txt","r")as file:
    #total lines
    strings = file.readlines()
    total_line = len(strings)
    #words in line
    words_line = list(map(lambda x: len(x.split()),strings))

    #total words in line
    total_words = reduce(lambda x,y: x+y,words_line)

    #line character
    strings = list(map(lambda x: x.strip(),strings))
    strings = list(map(lambda x:x.replace(" ",""),strings))
    line_character = list(map(lambda x:len(x),strings))

    #total character
    total_character = reduce(lambda x,y:x+y,line_character)

#save the answers in another file

with open("./module_7/practice_ans.txt","w")as file:
    file.write(f"Total lines:{total_line}\nTotal words:{total_words}\nTotal character:{total_character}")

    