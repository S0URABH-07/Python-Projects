import os
from src.quiz import QuizEngine

def main():
    data_directory = "data"
    file_path = os.path.join(data_directory, "quiz_data.json")
    
    if not os.path.exists(file_path):
        print(f"System Error: Please create the file at '{file_path}' first!")
        return
        
    print("=======================================")
    print("   WELCOME TO THE PYTHON QUIZ GAME    ")
    print("=======================================")
    input("Press Enter to start the game...")
    
    game = QuizEngine(file_path)
    
    # Main Game Loop: Keep going as long as there are questions left
    while game.has_more_questions() == True:
        current_q = game.get_next_question()
        
        current_q.display_question()
        
        while True:
            guess = input("\nYour Answer (A, B, C, or D): ").strip().upper()

            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please choose only A, B, C, or D.")
        
        game.check_player_guess(guess, current_q)
        print("-" * 40)
        
    final_percentage = game.calculate_percentage()
    print("\n================ GAME OVER ================")
    print(f"Final Score: {game.score} / {len(game.questions)}")
    print(f"Success Rating: {final_percentage:.1f}%")
    print("===========================================")

if __name__ == "__main__":
    main()