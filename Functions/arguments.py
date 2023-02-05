# def changeName(n):
#     n = "Yakup"


# name = "Gözde"

# changeName(name)  # It will not change, because it keeps its values
# print(name)


# def change(n):  # here, if we sent an array, list.. As we keep its address, it will change!!!!!!@@@@@
#     n[0] = "Istanbul"


# citites = ["Ankara", "Kayseri"]
# # change(citites) #here, it will change
# print(citites)

# # It was something like, a = b, if a[0] we change, it was affecting also b[0] as they are in the same address
# # We would take it like n = cities[:], n = list(cities)... so on
# # So, we can call the function like this:

# change(citites[:])  # Here, it will not change

# print(citites)

# If you want to send key-value relationship, use **params, if you want to use list, tuple.. you can use *params


# def add(a, b, c=0, d= 0,): ..... if we have a lot of value to send it to function, instead, do this:
# return sum((a, b, c))
def add(*params):
    print(params)
    print(params[1])
    return sum(params)


print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50, 60, 70))


def add2(*params):  # HERE, IT IS A TUPLE
    print(type(params))
    sum = 0
    for item in params:
        sum += item
    return sum


print(add2(2123, 4234, 123))


# What if we send parameters as data type? like name, price, city.... do this:
# ** means dictionary
def displayUser(**args):  # HERE, IT IS A DICTIONARY
    print(type(args))
    for key, value in args.items():
        print("{} - {}".format(key, value))


displayUser(name="Yakup", age=22, city="Kayseri")
displayUser(name="Gözde", age=21, city="Istanbul")

# What if we send data and *arg and **arg
def myFunc(a, b, *args, **kwargs):
    print("You callded mixed funciton")
    print(a)
    print(b)
    print(args)
    print(kwargs)


myFunc(10, 20, 30, 40, 50, key1="value 1", key2="value 2")
# 10 = a, 20 = b, [30,40,50] = *args, {key1="value1", key2 = "value2"} = **kwargs
