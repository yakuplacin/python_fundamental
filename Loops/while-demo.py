numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# i = 0
# while i < len(numbers):
#     print(numbers[i], end=" ")
#     i += 1

# start = int(input("Start: "))
# end = int(input("End: "))

# i = start
# while i <= end:
#     print(i)
#     i += 1

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# i = 0
# numbersArray = []
# while i < 5:
#     x = int(input(f"Number {i}"))
#     numbersArray.append(x)
#     i += 1

# numbersArray.sort()
# print(numbersArray)

producst = []
productCount = int(input("Product Count:"))

i = 0
while i < productCount:
    name = input("Product Name: ")
    price = float(input("Price: "))
    producst.append({

        "name": name,
        "price": price

    })
    i += 1

for product in producst:
    print(f"name: {product['name']} price: {product['price']}")
