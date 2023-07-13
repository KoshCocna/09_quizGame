class QuizBrain:

    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0

    def still_has_questions(self):
        if self.questionNumber < len(self.questionList):
            return True
        else:
            return False

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        user_answer = input(f"Q{self.questionNumber}:{currentQuestion.text} (True/False): ")
        self.check_answer(user_answer, currentQuestion.answer)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You're right!")
        else:
            print(f"You're wrong! the correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.questionNumber}\n")
