import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2  # adds corresponding values to each other
result = numbers1 + 10  # adds 10 to each term
result = numbers1 - numbers2
result = numbers1 - 10

result = np.sin(numbers1)  # takes each terms' sinus
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

mnumbers1 = numbers1.reshape(2, 3)
mnumbers2 = numbers2.reshape(2, 3)

print(mnumbers1)
print(mnumbers2)

# it combines both np arrays vertical
result = np.vstack((mnumbers1, mnumbers2))
# it combines both np arrays horizontal
result = np.hstack((mnumbers1, mnumbers2))

# controls each term if they are bigger than 5 and gives an array as [True True False....]
result = numbers1 >= 5

# controls each term if they are even or not
result = numbers1 % 2 == 0
print("the even numbers in numbers1: ")
# Here, result is a list as true false .. so if we use like this, it gives the true values
print(numbers1[result])

print(result)
