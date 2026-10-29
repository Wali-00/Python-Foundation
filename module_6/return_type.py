def name():
    print("wali")
print(type(name()))#nonetype

def adder(a,b):
    sum = a+b
    return sum
print(type(adder(10,20)))#int

def adder(a,b):
    return a,b
print(type(adder(10,20.9)))

#unzip
x,y=adder(10,20.8)
print(x,y)

