def sayHi(name="user"):
    # print("Hello World! its " + name)
    return "Hello " + name


msg = sayHi("Yakup")  # it will write "Yakup"
msg = sayHi()  # it will write "user" because we gave it to the function itself if there is no such a variable

print(msg)


def total(num1, num2):
    return num1 + num2


result = total(20, 41)
print(result)


def calculateAge(birthYear):
    return 2023 - birthYear


ageYakup = calculateAge(2000)
print(ageYakup)


def retireYear(birthDate, name):
    '''
    DOCSTRING: You can calculate how many years left to be retired.
    INPUT: Birthdate and name
    OUTPUTs: Calculated year(s) 
    '''
    age = calculateAge(birthDate)
    retired = 65 - age
    if (retired > 0):
        print(f"you have {retired} years to be retired")
    else:
        print("You have been already retired")


retireYear(1974, "Yakup")
retireYear(2012, "A")

print(help(retireYear))
