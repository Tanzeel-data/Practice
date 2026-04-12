import numpy as np

arr = np.arange(1, 11)
matrix = arr.reshape(2, 5)
row_sums = matrix.sum(axis=1)

print(matrix)
print(row_sums)