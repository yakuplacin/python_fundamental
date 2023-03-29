# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# q1 = Question("Which program is more useful for data science?",
#               ["C#", "JAVA", "JS", "Python"], "Python")

# q2 = Question("Which program is more populer?",
#               ["JAVA", "C#",  "Python", "JS"], "Python")

# q3 = Question("Which program's payment is the highest",
#               ["C#", "JS", "JAVA", "Python"], "Python")

# list = [q1, q2, q3]

# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("Java"))

# Quiz

class Quiz:
    def __init__(self, questions):
        self.qustions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.qustions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")


q1 = Question("Which program is more useful for data science?",
              ["C#", "JAVA", "JS", "Python"], "Python")

q2 = Question("Which program is more populer?",
              ["JAVA", "C#",  "Python", "JS"], "Python")

q3 = Question("Which program's payment is the highest",
              ["C#", "JS", "JAVA", "Python"], "Python")

questions = [q1, q2, q3]

quiz = Quiz(questions)

question = quiz.getQuestion()
# print(question.text)

quiz.displayQuestion()
