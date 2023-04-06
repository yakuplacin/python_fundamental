def calculate_grade(line):
    line = line[:-1]
    grList = line.split(":")
    studentName = grList[0]
    grades = grList[1].split(",")

    grades1 = int(grades[0])
    grades2 = int(grades[1])
    grades3 = int(grades[2])

    print(grades1)
    print(grades2)
    print(grades3)

    average = (grades1 + grades2 + grades3)/3

    if average >= 90 and average <= 100:
        grade = "A"
    elif average >= 87:
        grade = "A-"
    elif average >= 83:
        grade = "B+"
    elif average >= 80:
        grade = "B"
    elif average >= 77:
        grade = "B-"
    elif average >= 73:
        grade = "C+"
    elif average >= 70:
        grade = "C"
    elif average >= 64:
        grade = "C-"
    elif average >= 56:
        grade = "D+"
    elif average >= 50:
        grade = "D"
    elif average >= 0 and average <= 50:
        grade = "F"

    return studentName + ": " + grade + "\n"


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
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        gradeList = []

        for i in file:
            gradeList.append(calculate_grade(i))

        with open("results.txt", "w", encoding="utf-8") as file2:
            for i in gradeList:
                file2.write(i)


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
