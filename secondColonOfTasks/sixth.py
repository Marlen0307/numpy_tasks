import numpy as np

print("Original matrix:\n")
random_matrix = np.random.randint(0, 10, (3, 3))
print("The Rank of a Matrix: ", np.linalg.matrix_rank(random_matrix))
