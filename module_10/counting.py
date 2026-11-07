import numpy as np
a = np.random.randint(1,100,size=100,)
value_count = np.count_nonzero(a>90)
# unique_value = np.unique(a,return_counts=True)
unique_value,count= np.unique(a,return_counts=True)
print(unique_value)
print(count)