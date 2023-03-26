# x = "global x"


# def function():
#     x = 'local x'
#     print(x)


# function()
# print(x)


# name = "Yakup"


# def changeName(new_name):
#     name = new_name
#     print(name)


# changeName("Gözde")
# print(name)

########

name = "Global String"


def greeting():
    # name = "Yakup"

    def Hello():
        # name = "Gözde"
        print("Hello " + name)

    Hello()


greeting()

########

x = 50


def test():
    global x
    print(f'x {x}')

    x = 100
    print(f'changed to {x}')


test()
print(x)
