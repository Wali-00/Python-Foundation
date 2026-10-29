s = {10,20,30,40}
s_iter = iter(s)
print(type(s_iter))#set iterator

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

for i in s:
    print(i) #both are same

#iterator in dictionary
d = {"name":"wali","sub":"cse","roll":14}
d_iter = iter(d.items())
print(next(d_iter))
print(next(d_iter))
print(next(d_iter))

student ={
    "name": "Wali",
    "age": 24,
    "dept":"cse"
}
it = iter(student.items())
while True:
    try:
        key,value = next(it)
        print(key,":",value)
    except StopIteration:
        break

#another way
student= {
    "name": "wali",
    "age": 24,
    "dept":"cse"
}
it= iter(student.items())
key,value= next(it)
print(key,value)