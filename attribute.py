import numpy as np

#nd array creation
arr = np.array([1,2,3])#1d
arr1 = np.array([[1,2,3],[4,5,6]])#2d
arr2 = np.array([[[1,2,3],[4,5,6]],
                 [[7,8,9],[10,11,12]]
                 ])#3d

#attribute of nd array
print(arr.dtype)#datatype
print(arr.ndim)#dimension
print(arr.shape)#floor,row,column
print(arr.size)#array size