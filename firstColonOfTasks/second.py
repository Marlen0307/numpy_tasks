import numpy as np

random_array = np.random.random((5, 5))
print("Original matrix:")
print(random_array)
min_val = random_array.min()
max_val = random_array.max()
print("Minimum value is:" + str(min_val))
print("Maximum value is:" + str(max_val))
