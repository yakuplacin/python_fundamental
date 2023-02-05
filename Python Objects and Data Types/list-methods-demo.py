names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1997]

names.append("Cenk")
names.insert(0,"Sena")
names.remove("Deniz")
# del names[4]
# names.pop()
# names.pop(2) #deletes the 3rd (second index) word


# isIn = "Ali" in names
isIn = names.index("Ali")
print(isIn)



names.reverse()
years.reverse()
years.sort()
names.sort()
print(names)
print(years)

str = "Chevrolet,Dacia"
str = str.split(",")
print(str)

print(max(years))
print(min(years))

print(years.count(1998))
years.clear()
print(years)

x = []
i = 0
while i in range(3):
    q = input(f"Number {i+1}: ")
    x.append(q)
    i = i + 1

print(x)

index = names.index("Hakan")
print(index)

names.pop(index) #deletes the "Hakan" means 2nd index