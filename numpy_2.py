import numpy as np

sales = np.arange(1, 11)

matrix = sales.reshape(2, 5)
print(matrix)

sum_of_sales = matrix.sum(axis=1)
print(sum_of_sales)

avg = sales.mean()
print(avg)

mn = sales.min()
mx = sales.max()


normalized = (sales - mn) / (mx - mn)
print(normalized)

filtered = sales[sales > 5]
print(filtered)

bonus = 10 + sales
print(bonus)

multiplied = sales * 2
print(multiplied)


