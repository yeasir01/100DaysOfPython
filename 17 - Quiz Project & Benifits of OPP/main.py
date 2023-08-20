from data import question_data
from question_model import Question
from quiz_brain import GameLogic

question_bank = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

game = GameLogic(question_bank)

while game.still_has_questions():
    game.next_question()

print("You've completed the quiz.")
print(f"Final Score: {game.score}/{game.question_number}")