def check_even(num):
    return num % 2 == 0


def check_even_lambda(num): return num % 2 == 0


numbers = [1, 2, 4, 3, 5, 7, 9]

result = list(filter(check_even, numbers))
print(result)

print(result[1])

# result = list(filter(check_even, numbers))
# result2 = list(filter(lambda num: num % 2 == 0, numbers))
# print(result)
# print(result2)
