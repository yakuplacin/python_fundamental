# class

class Person:

    # class attributes
    address = 'no information'

    # constructor (yapıcı method) initte çalışır, her classın objesine verir

    # self is the object itself, like p1 as we create. You can change the name whatever you want
    def __init__(self, name, year):
        # object attributes
        self.name = name
        # self.birthYear = year??
        self.year = year
        print("init is progressed")

        # methods


# object (instance)
p1 = Person(name="Yakup", year=2000)
p2 = Person("Gözde", 2001)

# updating
p1.name = "Yakup LAÇIN"
p1.address = "Türkiye"

# accesing object
print(f'p1 name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)

print(type(p1))
