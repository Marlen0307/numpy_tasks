import numpy as np

print("Original matrix:\n")
random_matrix = np.random.randint(0, 15, (4, 4))
print(random_matrix)
print("\nSorted matrix by nth column: ")
print(random_matrix[random_matrix[:, 1].argsort()])
