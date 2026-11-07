import numpy as np
x = np.array([10,20,30])
y = np.array([1,2,3])
greater_then = x>y
equal = x==y
print(greater_then)
# all() sob true kina
# any() jekono ekta true ase kina
print(np.all(greater_then))
print(np.any(equal))