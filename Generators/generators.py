def cube():
    for i in range(5):
        yield i ** 3


# generator = cube()
# iterator = iter(generator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# iterator = cube()
for i in cube():
    print(i)

# this is a normal array list that takes memory, and it prints all of the elements
aList = [i**3 for i in range(5)]
print(aList)

generator = (i**3 for i in range(5))
print(generator)  # this will print just object generator, isn't kept in memory
for i in generator:
    print(i)
