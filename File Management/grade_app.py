def calculate_grade(line):
    line = line[:-1]
    grList = line.split(":")
    studentName = grList[0]
    grades =


def read_average():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


def give_grade():
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    grade1 = input("Grade 1:")
    grade2 = input("Grade 2:")
    grade3 = input("Grade 3:")

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(name + " " + surname + ": " + grade1 +
                   ", " + grade2 + ", " + grade3 + "\n")


def save_grade():
    pass


while True:
    process = input("1- Read Grades\n2- Give Grades\n3- Save Grades\n4- Exit")

    if process == "1":
        read_average()
    elif process == "2":
        give_grade()
    elif process == "3":
        save_grade()
    else:
        break
