import tkinter as tk
import os
from src.snake import Snake
from src.food import Food

class GameWindow:
    def __init__(self, width=600, height=400, block_size=20):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.game_speed = 100 
        self.score = 0
        self.game_over = False
        
        self.score_file = "data/high_score.dat"
        self.high_score = self.load_high_score()

        self.snake = Snake(block_size=self.block_size)
        self.food = Food(window_width=self.width, window_height=self.height, block_size=self.block_size)

        self.root = tk.Tk()
        self.root.title("Snake Game Engine - Python Core")
        self.root.resizable(False, False)  

        self.score_label = tk.Label(
            self.root, 
            text=f"Score: {self.score}  |  High Score: {self.high_score}", 
            font=("Consolas", 14), 
            bg="black", 
            fg="white"
        )
        self.score_label.pack(fill="x")

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="#111111")
        self.canvas.pack()

        self.bind_keyboard_controls()

    def load_high_score(self):
        if os.path.exists(self.score_file):
            try:
                with open(self.score_file, "r") as file:
                    return int(file.read().strip())
            except:
                return 0
        return 0

    def save_high_score(self):
        log_dir = os.path.dirname(self.score_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        with open(self.score_file, "w") as file:
            file.write(str(self.high_score))

    def bind_keyboard_controls(self):
        self.root.bind("<Up>", lambda e: self.snake.change_direction([0, -self.block_size]))
        self.root.bind("<Down>", lambda e: self.snake.change_direction([0, self.block_size]))
        self.root.bind("<Left>", lambda e: self.snake.change_direction([-self.block_size, 0]))
        self.root.bind("<Right>", lambda e: self.snake.change_direction([self.block_size, 0]))

    def verify_collisions(self):
        head_x, head_y = self.snake.coordinates[0]

        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True

        if [head_x, head_y] in self.snake.coordinates[1:]:
            return True

        return False

    def update_frame_tick(self):
        if self.game_over:
            return

        self.snake.move()

        if self.verify_collisions():
            self.game_over = True
            self.display_game_over_screen()
            return

        head_coords = self.snake.coordinates[0]
        if head_coords == self.food.coordinates:
            self.snake.grow()
            self.score += 10
            
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
                
            self.score_label.config(text=f"Score: {self.score}  |  High Score: {self.high_score}")
            self.food.spawn_new_location(self.snake.coordinates)

        self.repaint_canvas()

        self.root.after(self.game_speed, self.update_frame_tick)

    def repaint_canvas(self):
        self.canvas.delete("all")

        fx, fy = self.food.coordinates
        self.canvas.create_oval(
            fx, fy, fx + self.block_size, fy + self.block_size, 
            fill="#FF3333", outline="#990000"
        )

        for index, (x, y) in enumerate(self.snake.coordinates):
            color = "#33FF33" if index == 0 else "#22CC22"
            self.canvas.create_rectangle(
                x, y, x + self.block_size, y + self.block_size, 
                fill=color, outline="#116611"
            )

    def display_game_over_screen(self):
        self.canvas.create_text(
            self.width // 2, self.height // 2, 
            text="GAME OVER", font=("Consolas", 30, "bold"), fill="#FF3333"
        )
        self.canvas.create_text(
            self.width // 2, (self.height // 2) + 40, 
            text="Press Spacebar to Restart Quest", font=("Consolas", 12), fill="white"
        )
        self.root.bind("<space>", lambda e: self.reset_game_state())

    def reset_game_state(self):
        self.score = 0
        self.game_over = False
        self.score_label.config(text=f"Score: {self.score}  |  High Score: {self.high_score}")
        
        self.snake = Snake(block_size=self.block_size)
        self.food.spawn_new_location(self.snake.coordinates)
        
        self.root.bind("<space>", lambda e: None) 
        self.update_frame_tick() 

    def launch(self):
        self.update_frame_tick()
        self.root.mainloop()    