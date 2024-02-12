#Create a class for creating quiz
#
class QuizBrain:

# Initialize the attribites
    def __init__(self, q_list):
        self.question_number = 0  # Default value of 0
        self.score = 0
        self.question_list =  q_list      # Get it as a value passed over


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right')
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print('You got it wrong')
            print(f"Your current score is: {self.score}/{self.question_number}")
        print(f'The correct answer was: {correct_answer}')
        print(f"Your answer was: {user_answer}")
        print("\n\n\n")

