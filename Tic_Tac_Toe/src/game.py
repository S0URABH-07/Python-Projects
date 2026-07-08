import tkinter as tk
from tkinter import messagebox
from src.logic import TicTacToeLogic

class TicTacToeGUI:
    def __init__(self):
        self.engine = TicTacToeLogic()
        self.game_locked = False

        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe Engine - Python Core")
        self.root.resizable(False, False)

        self.score_label = tk.Label(
            self.root,
            text=self.get_score_string(),
            font=("Consolas", 12, "bold"),
            bg="#222222",
            fg="white",
            pady=8
        )
        self.score_label.pack(fill="x")

        self.grid_frame = tk.Frame(self.root, bg="black")
        self.grid_frame.pack()

        self.buttons = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        
        self.initialize_button_grid()

    def get_score_string(self):
        s = self.engine.scores
        # return f"Turn: Player {self.engine.current_player}  |  Wins X: {s['X']}  |  Wins O: {s['O']}  |  Ties: {s['Ties']}"

    def initialize_button_grid(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(
                    self.grid_frame,
                    text="",
                    font=("Consolas", 24, "bold"),
                    width=6,
                    height=2,
                    bg="#FFFFFF",
                    activebackground="#EEEEEE",
                    command=lambda row=r, col=c: self.handle_square_click(row, col)
                )
                self.buttons[r][c].grid(row=r, column=c, padx=4, pady=4)

    def handle_square_click(self, row, col):
        if self.game_locked:
            return

        move_success = self.engine.make_move(row, col)
        
        if move_success == True:
            active_token = self.engine.current_player
            self.buttons[row][col].config(
                text=active_token, 
                fg="#FF3333" if active_token == "X" else "#3333FF"
            )
            
            winner = self.engine.check_winner()
            if winner != None:
                self.game_locked = True
                self.engine.update_scores(winner)
                messagebox.showinfo("Match Concluded", f"Congratulations! Player {winner} secures victory! ")
                self.reset_match_cycle()
                return

            if self.engine.is_board_full():
                self.game_locked = True
                self.engine.update_scores("Ties")
                messagebox.showinfo("Match Concluded", " Stale State! The match ends in a Tie.")
                self.reset_match_cycle()
                return

            self.engine.toggle_player()
            self.score_label.config(text=self.get_score_string())

    def reset_match_cycle(self):
        self.engine.reset_board_state()
        self.game_locked = False
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", bg="#FFFFFF")
                
        self.score_label.config(text=self.get_score_string())

    def launch(self):
        self.root.mainloop()