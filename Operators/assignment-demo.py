x, y, z = 2, 5, 10



# nm1 = int(input("number1: "))
# nm2 = int(input("number2: "))

# total1 = nm1*nm2
# total2 = x+y+z
# print(total2-total1)

# print(y//x)

result = (x + y + z)%3
print(result)
print(y**x)

numbers = 1, 5, 7, 10, 6  
x, *y, z = numbers  # y will be [5,7,10], x will be 1 (first), z will be 6 (last)
print(z**3)

result = 0
for i in y:
    result += i

print(result)