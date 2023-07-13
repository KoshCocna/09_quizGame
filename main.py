from questionModel import Question
from data import question_data
from quizBrain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQuestion = Question(question_text, question_answer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()