import json
import os
from src.question import Question

class QuizEngine:
    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = []
        self.score = 0
        self.current_question_index = 0
        
        self.load_questions()

    def load_questions(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                raw_data = json.load(file)
                
                for item in raw_data:
                    new_question = Question(
                        question_text=item["question"],
                        options=item["options"],
                        correct_answer=item["answer"]
                    )
                    self.questions.append(new_question)
        else:
            print("Error: Questions data file could not be found!")

    def has_more_questions(self):
        if self.current_question_index < len(self.questions):
            return True
        else:
            return False

    def get_next_question(self):
        if self.has_more_questions() == True:
            current_q = self.questions[self.current_question_index]
            return current_q
        return None

    def check_player_guess(self, user_guess, current_question):
        if current_question.check_answer(user_guess) == True:
            print("Correct Answer! Well done.")
            self.score = self.score + 1
        else:
            print(f"Incorrect! The correct answer was: {current_question.correct_answer}")
            
        self.current_question_index = self.current_question_index + 1

    def calculate_percentage(self):
        total_q = len(self.questions)
        if total_q == 0:
            return 0.0
        return (self.score / total_q) * 100