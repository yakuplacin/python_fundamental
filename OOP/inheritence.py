# Inheritence (Kalıtım) - (Miras Alma)

# Person => name, lastname, age, eat(), drink(), run()
# Student(Person), Teacher(Person) will take all person features. We do not need to create Person again.


# Animal => Dog(Animal), Cat(Animal) another example.

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_are_you(self):
        print(f"I am the person called: {self.firstName}")

    def eat(self):
        print("I am eating")


class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")

    def who_are_you(self):
        print(f"I am the student called: {self.firstName}")

    def sayHi(self):
        print("I am a student, from class")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  # we can also do like that
        self.branch = branch

    def who_are_you(self):
        print(f"I am a {self.branch} teacher")


p1 = Person('Gözde', 'AĞAR')
p2 = Student('Yakup', 'LAÇIN', 4464)
t1 = Teacher("Doruk", "LAÇIN", "Computer")
print(p1.firstName + " " + p1.lastName)
print(p2.firstName + " " + p2.lastName + " " + str(p2.studentNumber))

p1.who_are_you()
p2.who_are_you()
p1.eat()
p2.sayHi()

t1.who_are_you()
