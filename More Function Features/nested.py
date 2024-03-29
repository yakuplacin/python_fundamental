# def greeting(name):
#     print("Hello, ", name)

# sayHello = greeting

# del sayHello
# print(greeting)

# encapsulation
def outer(num1):
    print("outer")

    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)


outer(10)


def factorial(number):

    if not isinstance(number, int):
        raise TypeError("Number should be an integer")

    if not number >= 0:
        raise ValueError("Number should be positive or zero")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

# More simplified one
# def factorial(number):

#     if not isinstance(number, int):
#         raise TypeError("Number should be an integer")

#     if not number >= 0:
#         raise ValueError("Number should be positive or zero")

#     if number <= 1:
#         return 1
#     return number * factorial(number - 1)


try:
    print(factorial(-4))
except Exception as ex:
    print(ex)
