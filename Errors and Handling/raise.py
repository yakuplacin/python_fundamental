# x = 20

# if x > 4:
#     raise Exception("X cannot be greater than 4")

# def checkPassword(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Password must be at least 8 character")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Password should include lower case")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Password should include upper case")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Password should include numeric value")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Password should include alpha numeric value")
#     elif re.search("\s", psw):
#         raise Exception("Password should not contain space")


# password = "aA123456$"

# try:
#     checkPassword(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Accepted Password")
# finally:
#     print("Validation has been done!")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name has too much character")
        else:
            self.name = name


p = Person("ThisIsMyName", 2023)
