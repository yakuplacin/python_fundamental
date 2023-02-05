carList = ["BMW","Mercedes", "Opel", "Mazda"]
print(len(carList))

print(carList[0] + " " + carList[-1])

carList[3] = "Toyota"
print(carList)

x = carList.__contains__("Mercedes")
y = "Mercedes" in carList #returns True or False
print(x)
print(y)

print(carList[-2])

print(carList[0:3])
print(carList[:3])

carList[-2:] = ["Toyota", "Renault"]
print(carList)
carList = carList + ["Audi", "Nissan"]
print(carList)
carList.append("Mitsubishi")
print(carList)

# carList.remove(carList[-1])
del carList[-1]
print(carList)

# carList.reverse()
carList = carList[::-1]
print(carList)

studentA = ["Yakup", "LAÇIN", 2022, [101,77,100]]
studentB = ["Gözde", "X", 2022, [90, 90, 90]]
studentC = ["Senim","Y", 2028, [100, 100, 100]]

studentList = [studentA, studentB, studentC]
print(studentList[2])

