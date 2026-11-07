import numpy as  np
a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([[2,3],[32,32],[23,3]])
dot_product = np.dot(a,b)
print(dot_product)
print(np.trace(b))#sum of diagonal

#determinate
b = np.array([[2,3],[32,32]])
print(np.linalg.det(b))