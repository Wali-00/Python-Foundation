import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0])
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1[0][1]) # row then column

arr2 = arr1 #if we change a value in arr2 or arr1 it will change in both array..we can use copy method to avoid this problem
arr3 = arr1.copy()
print(arr2)
arr2[0][1]= 100
print(arr1) 
print(arr3)