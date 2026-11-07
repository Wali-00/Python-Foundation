import numpy as np

x = np.array([2,1,4,2,49,34,59])
#np.where in 1d (condition,x,y) if true x,otherwise replace with y
index = np.where(x==2) #return index
print(index)
array  = np.where(x>8,x,0) #return array
print(array)

#max
max_value = np.max(x)
print(max_value)
#min
min_value = np.min(x)
print(min_value)
#max index
max_value_index = np.argmax(x)
print(max_value_index)
min_value_index = np.argmin(x)
print(min_value_index)