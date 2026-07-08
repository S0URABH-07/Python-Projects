class TicTacToeLogic:
    def __init__(self):
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.reset_board_state()

    def reset_board_state(self):
        self.current_player = "X"
        
        self.board = [
            ["", "", ""],  # Row 0
            ["", "", ""],  # Row 1
            ["", "", ""]   # Row 2
        ]

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            return True
        return False

    def toggle_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        b = self.board

        for r in range(3):
            if b[r][0] == b[r][1] == b[r][2] != "":
                return b[r][0]

        for c in range(3):
            if b[0][c] == b[1][c] == b[2][c] != "":
                return b[0][c]

        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]

        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]

        return None

    def is_board_full(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    return False 
        return True

    def update_scores(self, result_type):
        if result_type in self.scores:
            self.scores[result_type] = self.scores[result_type] + 1