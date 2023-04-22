import numpy as np

np_array = np.array([10, 15, 30, 45, 60])
np_array = np.arange(5, 15)
np_array = np.arange(50, 100, 5)
np_array = np.zeros(10)
np_array = np.ones(10)
np_array = np.linspace(0, 100, 5)
np_array = np.random.randint(10, 30, 5)
np_array = np.random.randn(10)

matrix = np.random.randint(-50, 50, 15).reshape(3, 5)
print(matrix)
rowTotal = matrix.sum(axis=1)
colTotal = matrix.sum(axis=0)
print(rowTotal)
print(colTotal)

result = matrix.max()
result = matrix.min()
result = matrix.mean()

result = matrix.argmax()
result = matrix.argmin()

arr = np.arange(10, 20)
print(arr)
result = arr[0:3]
result = arr[::-1]

result = matrix[0]
result = matrix[1, 2]
result = matrix[:, 0]
result = matrix ** 2

evens = matrix[matrix % 2 == 0]
result = evens[evens > 0]
print(result)
