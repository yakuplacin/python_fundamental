students = {}

number = (input("Student number: "))
name = (input("Student name: "))
surname = (input("Student surname: "))
phone = (input("Student phone: "))

# students[number] = {
#     "name": name,
#     "surname": surname,
#     "phone": phone
# }

students.update({
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})
number = "212"
name = "Gözde"
students.update({
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})
number = "512"
name = "Senim"
students.update({
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})

print(students)

studentNumber = input("Student no you try to find: ")
student = students[studentNumber]

print(f"The student you try to find with number {studentNumber} name: {student['name']} and surname: {student['surname']}")
