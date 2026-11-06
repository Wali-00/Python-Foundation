import numpy as np

#list to ndarray
lis = [1,2,3]
arr = np.array(lis)

mixed_lis = [1,2.3,"hello"]
arr1 = np.array(mixed_lis)

#tuple to ndarray

tup =(1,2,3)
arr2= np.array(tup,dtype=np.int16)

#we cannot covert set into ndarray

#dict to ndarray
dic = {"a":1,"b":2,"c":3}

keys = dic.keys()
values = dic.values()
items = dic.items()

arr3 = np.array(list(keys))
arr4 = np.array(list(values))
arr5 = np.array(list(items))