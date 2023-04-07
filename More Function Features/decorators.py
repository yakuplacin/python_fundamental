import time
import math


def my_decorator(func):
    def wrapper():
        print("The state that is before the function")
        func()
        print("The state that is after the function")
    return wrapper


@my_decorator  # Send this to the my_decorator function as a parameter.
def sayHello():
    print("Hello!")

# def sayGreeting():
#     print("Greeting!")

# Instead this, write @my_decorator to the beginning of the function, it will put the function to the decorator.
# Hello = my_decorator(sayHello)
# Hello()


# Greeting = my_decorator(sayGreeting)
# Greeting()
sayHello()


def calculateTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Functino took " + func.__name__ + " " + str(finish-start))

    return inner


@calculateTime
def takePower(a, b):
    # start = time.time()
    # time.sleep(1)
    print(math.pow(a, b))
    # finish = time.time()
    # print("Functino took " + str(finish-start))


@calculateTime
def factorial(num):
    # start = time.time()
    # time.sleep(1)
    print(math.factorial(num))
    # finish = time.time()
    # print("Functino took " + str(finish-start))


takePower(2, 3)
factorial(4)
