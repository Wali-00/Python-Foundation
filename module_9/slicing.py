import numpy as np
arr = np.array([8,9,10,11,12])
# [start:end:step]
arr1 = arr[0:3] #1d array

# [row start : row end : step : column start: column end: step]

arr = np.array([[1,2,4],[5,6,7]])
row_1 = arr[0:1,] #0-1 row and all column
row_2 = arr[1:,]#after first row print the other

col_1 = arr[ : ,0:1]

col_2 = arr[:,1:2]

col_3 = arr[:,2:]




