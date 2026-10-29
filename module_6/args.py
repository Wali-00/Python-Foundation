def adder(*args):
    print(args[0])

adder(19,132,1)

def adder(*args):
    for i in args:
        print(i)

adder(23,34,54)

def adder(a,b,c):
    print(f"{a},{b},{c}")

adder(c=2,b=3,a=1)


def adder(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

adder(a=1,b=2,c=3)

