numbers = [1,5,34,123,4,1,5,10,23,5]
letters = ["a", "g", "y", "a","y","u","s","e","n"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)


val = numbers[3:6]
val = numbers[::-1]

numbers[3] = 222

numbers.append(99) #adds to the end of the array
numbers.append(291)

numbers.insert(3,77) #adds the right of value's (here 3rd index) index
numbers.insert(-1,14) #adds last-1 because it puts before the index, (here -1 means final), so it will be the before the last
numbers.pop() #deletes the last item in the array
numbers.pop(2) #deletes the which index inside it
numbers.sort()
letters.sort()

numbers.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(numbers.count(5)) #how many 5 we have, count and print
print(letters.count("a"))

numbers.clear() #deletes all elements of the array