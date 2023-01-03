import numpy as np

random_matrix = np.ones((16, 16))
k = 4
block_sum = np.add.reduceat(np.add.reduceat(random_matrix, np.arange(0, random_matrix.shape[0], k), axis=0),
                            np.arange(0, random_matrix.shape[1], k), axis=1)
print("Original:\n")
print(random_matrix)
print("Block-sum matrix\n")
print(block_sum)
