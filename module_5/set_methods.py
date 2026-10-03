s = {10,20,50,40,30}
print(type(s))
s.add(35)
print(s)

s.pop()#pop first element
print(s)
s.remove(10) #remove specific value
print(s) 

a = {1,2,3}
b = {4,5,6}
c = a.union(b) #union
print(c)

print(a.intersection(c)) #intersection

#disjoint
print(a.isdisjoint(b))
#issubset
print(a.issubset(c))