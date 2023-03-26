# lambda num: num **2 # returns n^2
def square(num): return num**2


numbers = [1, 3, 5, 7, 9]

result = list(map(square, numbers))
print(result)

result = square(12)
print(result)
