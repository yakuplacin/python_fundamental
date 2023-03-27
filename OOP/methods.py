# # class

# class Person:

#     # class attributes
#     address = 'no information'

#     # constructor (yapıcı method) initte çalışır, her classın objesine verir
#     # self is the object itself, like p1 as we create. You can change the name whatever you want
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.year = year

#     # instance method
#     def intro(self):
#         print("Hello, I'm a method! I am person: " + self.name)

#     # instance method
#     def calculateAge(self):
#         return 2023 - self.year


# # object (instance)
# p1 = Person(name="Yakup", year=2000)
# p2 = Person("Gözde", 2001)

# p1.intro()
# p2.intro()

# print("The age is: " + str(p2.calculateAge()))


class Circle:
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def circumferenceCalculate(self):
        return 2*self.pi*self.radius

    def areaCalculate(self):
        return self.pi * (self.radius**2)


c0 = Circle()  # radius = 1
c1 = Circle(5)

print(f'Circumference of c1: {c1.areaCalculate()}')
