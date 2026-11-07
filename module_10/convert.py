#convert into row flatting
import numpy as np
array = np.random.randint(1,10, size=(10,5))

flatten = array.flatten()

#another way
row_flatten = np.ravel(array,order="F")

column_flatten = np.ravel(array, order = "C")

