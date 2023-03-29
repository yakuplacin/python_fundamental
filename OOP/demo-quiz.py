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
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('-' + q)

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz is finished")
        else:
            print(f"Question {questionNumber} of {totalQuestion}")


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

# quiz.displayQuestion()

quiz.loadQuestion()
