def takePower(number):

    def inner(power):
        return number ** power

    return inner


# Here, this will return inner function that returns number ** power and it takes the power parameter
two = takePower(2)
three = takePower(3)

print(two(3))
print(three(4))


def askPermission(page):
    def innerFunction(role):
        if role == "Admin":
            return "{0} role can achieve page {1}".format(role, page)
        else:
            return "{0} role cannot achieve page {1}".format(role, page)
    return innerFunction


user1 = askPermission("Product Edit")
print(user1("Admin"))
print(user1("User"))


def process(process_name):
    def add(*args):
        total = 0
        for i in args:
            total += i
        return total

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result
    if process_name == "addition":
        return add
    else:
        return multiply


addition = process("addition")
print(addition(1, 3, 6, 5, 10, 15, 10))

multiply = process("multiply")
print(multiply(6, 4, 5, 3, 1, 2))
