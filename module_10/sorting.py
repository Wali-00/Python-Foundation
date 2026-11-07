import numpy as np
#inplace
x = np.array([2,1,4,2,49,34,59])
y = x.copy()
y.sort()
print(y)
print(x)

#with function
x = np.array([2,1,4,2,49,34,59])
y = np.sort(x)
print(y)
print(x)

#2d array sort
#horizon axis =1
#vertical axis = 0
mat = np.array([[10,3,5],[8,4,9]])
horizon = np.sort(mat,axis=1)
vertical = np.sort(mat,axis=0)
print(horizon)
print(vertical)