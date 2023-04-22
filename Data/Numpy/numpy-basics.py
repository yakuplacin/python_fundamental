import numpy as np

# python list
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numpy array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print(type(np_array))

py_multiList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_multiArray = np_array.reshape(3, 3)

print(np_multiArray)
print(py_multiList)

print(np_array.ndim)
print(np_multiArray.ndim)

print(np_array.shape)
print(np_multiArray.shape)
