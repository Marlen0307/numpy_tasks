import numpy as np

array = np.random.uniform(0, 10, 10)

print(array - array % 1)
print(array // 1)
print(np.floor(array))
print(array.astype(int))
print(np.trunc(array))
