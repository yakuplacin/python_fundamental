import datetime
# name = input("name: ")
# age = int(input("age: "))
# education = input("education: ")

# if (age >= 18) and (education == "high school" or education == "university"):
#     print("You can take the driver licence!")
# else:
#     print("You do not provide the sufficient documents")

# mt1 = float(input("midterm1: "))
# mt2 = float(input("midterm2: "))
# final = float(input("final: "))

# average = (mt1 + mt2 + final) / 3
# result = 0
# if (average <= 24) and (average >= 0):
#     result = 0
# elif (average <= 44) and (average > 24):
#     result = 1
# elif (average <= 54) and (average > 44):
#     result = 2
# elif (average <= 69) and (average > 54):
#     result = 3
# elif (average <= 84) and (average > 69):
#     result = 4
# elif (average <= 100) and (average > 84):
#     result = 5

# print(result)

carDateYear = int(input("car traffic Date Year: "))
carDateMonth = int(input("Which month: "))
carDateDay = int(input("Which day: "))

x = datetime.datetime(carDateYear, carDateMonth, carDateDay)
y = datetime.datetime.now()
print(x,y)
d = y - x
print(d.days)
result = d.days / 365

if result < 1:
    print("birinci bakım")
elif result < 2:
    print("ikinci bakım")
elif result < 3:
    print("ÜÇÜNCÜ BAKIM")
