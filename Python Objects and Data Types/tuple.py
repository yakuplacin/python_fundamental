list  = [1, 2, 5, 7, 6]
tuple = ("bir", 2, 3, "4")

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[0])

print(len(list))
print(len(tuple))

list = ["Yakup", "Gözde"]
tuple = ("Emre", "Şeyma")

print(list)
print(tuple)

list[0] = "Pukay" #we can chane list item with this but we cannot change in the tuple:
# tuple[0] = "Senim"  we cannot give this!!!!

names = ("Yakup", "Gözde") + tuple
print(names)