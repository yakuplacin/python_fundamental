#what does map do? : it sends list's elements one by one to the function

def square(num): return num ** 3
numbers = [1, 3, 5, 9]

result = list(map(square, numbers))
# result = square(24)
print(result)

# we should use map with list or in the for loop to take it as enumarate (it means, every item should be visited and taken)

for item in map(square, numbers):
    print(item)
