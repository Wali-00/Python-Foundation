import numpy as np

arr = np.random.rand(3,2)
print(np.random.rand())#0–1 এর মধ্যে random decimal
print(np.random.rand(5))#5টি random decimal
print(np.random.rand(2,3))#2×3 random array
print(np.random.randint(1,10))#1 থেকে 9 পর্যন্ত random integer

print(np.random.uniform(10,20,(2,4)))