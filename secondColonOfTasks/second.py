import numpy as np

A = np.random.randint(1, 3, 7)
print("First array:")
print(A)
B = np.random.randint(1, 3, 7)
print("Second array:")
print(B)
print("Are the arrays equal?")
array_equal = np.allclose(A, B)
print(array_equal)
