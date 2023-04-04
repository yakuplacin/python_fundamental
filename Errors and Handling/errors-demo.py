myList = ["11", "22", "as1", "sdj2", "92", "84"]

# Add numbers in the list to a new list
myList2 = []
for x in myList:
    try:
        result = int(x)
        myList2.append(result)
    except ValueError:
        continue
print(myList2)

# Until user press q, try to take number, if it is not numeric value, throw an exception
while True:
    number = input("Number: ")
    if number == "q":
        break
    try:
        result = float(number)
        print("Your number: ", number)
    except ValueError:
        print("Non-accepted number")
        continue

# Check if a password include Turkish character


def checkPassword(password):

    turkish_chars = "şçğüoıİ"
    for i in password:
        if i in turkish_chars:
            raise TypeError("Password cannot include Turkish characters")
        else:
            pass
    print("Accepted password")


password = input("password: ")
try:
    checkPassword(password)
except TypeError as err:
    print(err)


# Calculate the factorial of given input if it is a numeric value
def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negative Value")

    result = 1

    for i in range(1, x+1):
        result *= i

    return result


for x in [5, 7, 10, -23, "sf2"]:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
