def addition(a, b):
    return a + b


def multiply(a, b):
    return a * b


def substract(a, b):
    return a - b


def division(a, b):
    return a / b


def process(f1, f2, f3, f4, process_name, num1, num2):
    if process_name == "addition":
        print(f1(num1, num2))
    elif process_name == "substract":
        print(f2(num1, num2))
    elif process_name == "multiply":
        print(f3(num1, num2))
    elif process_name == "division":
        print(f4(num1, num2))
    else:
        print("Unsuccess Process")


process(addition, substract, multiply, division, "addition", 10, 2)
process(addition, substract, multiply, division, "substract", 10, 2)
process(addition, substract, multiply, division, "multiply", 10, 2)
process(addition, substract, multiply, division, "division", 10, 2)
process(addition, substract, multiply, division, "mode??", 10, 2)
