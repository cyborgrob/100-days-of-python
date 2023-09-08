class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Displays the questions in a sequence"""
        # question_list is a list of Question objects, so 'question' variable is a Question object
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        # since 'question' is a Question object, we can access its answer with question.answer
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        """Checks if we're at the end of the list of questions"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks whether user's answer is right or wrong"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")




