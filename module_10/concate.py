#concatenate
#row wise concatenate korar shomoi column same thkbe
# column wise concatenate krar shomoi row same thkbe
import numpy as np
a = np.random.randint(1,10, size=(2,3))
b = np.random.randint(10,20, size=(2,3))

concate_row= np.concatenate((a,b),axis=0)#row wise
concate_column= np.concatenate((a,b),axis=1)#column wise

#transpose

mat = np.array([[10,20,30],[40,50,60]])
tran = mat.T
