myList = [1, 2, 3, 4, 5]

iterator = iter(myList)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# # for loop does iterator automatically for us
# for i in myList:
#     print(i)


# for loop do this like that:
iterator = iter(myList)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

print("------------------------------")


class MyNumbers:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


IterList = MyNumbers(20, 50)

# for x in IterList:
#     print(x)

myIter = iter(IterList)
while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break
