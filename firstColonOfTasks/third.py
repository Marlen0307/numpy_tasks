import numpy as np

randomized_matrix = np.random.random((5, 5))
print("Original matrix:")
print(randomized_matrix)
max_val = randomized_matrix.max()
min_val = randomized_matrix.min()
x = (randomized_matrix - min_val) / (max_val - min_val)
print("After normalization:")
print(x)
