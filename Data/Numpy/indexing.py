import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]
result = numbers[::-2]

numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
result = numbers2[2]  # gives [50 75 85]
result = numbers2[0, 2]  # gives 10
result = numbers2[2, 1]  # gives 75
result = numbers2[:, 2]  # gives [10 25 85]
result = numbers2[:, 0]  # gives [0 15 50]
result = numbers2[:, 0:2]  # gives [[ 0  5] [15 20] [50 75]]
result = numbers2[-1, :]  # gives [50 75 85]
result = numbers2[:3, :2]  # gives [[0 5] [15 20] [50 75]]

print(result)

arr1 = np.arange(0, 10)
arr2 = arr1  # referance

print(arr1)
print(arr2)

arr2[0] = 20  # This will change both arr1 and arr2's first value to the 20 as they share the same memory place

print(arr1)
print(arr2)

# So, we can do like this:
arr2 = arr1.copy()
print(arr1)
print(arr2)

arr2[0] = 99
print("After set arr2 first value to 99")
print(f"arr1 {arr1}")
print(f"arr2 {arr2}")
