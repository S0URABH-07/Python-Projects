class Question:
    def __init__(self, question_text, options, correct_answer):
        # Setting up the core variables for an individual question card
        self.question_text = question_text
        self.options = options

        self.correct_answer = correct_answer.strip().upper()

    def check_answer(self, user_guess):

        cleaned_guess = user_guess.strip().upper()
        
        if cleaned_guess == self.correct_answer:
            return True
        else:
            return False

    def display_question(self):
        print(f"\n{self.question_text}")
        for option in self.options:
            print(option)