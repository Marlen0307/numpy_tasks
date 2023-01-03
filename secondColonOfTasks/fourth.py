import numpy as np

print("Original matrix:\n")
matrix = np.random.rand(5, 10)
print(matrix)
print("\nSubtract the mean of each row of the given matrix:\n")
subtracted_matrix = matrix - matrix.mean(axis=1, keepdims=True)
print(subtracted_matrix)
