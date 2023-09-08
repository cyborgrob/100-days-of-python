from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank full of Question objects, each with question text and answer
question_bank = []

# For each item in the question_data list, appending the question_bank with a Question object with 'text' and 'answer'
for entry in question_data:
    # Since question_data is a dictionary, we pull the info using the relevant keys
    question = Question(entry['question'], entry['correct_answer'])
    question_bank.append(question)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print(f"You've completed the quiz. Your final score was: {brain.score}/{brain.question_number}")

