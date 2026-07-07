import random

class Food:
    def __init__(self, window_width=600, window_height=400, block_size=20):
        self.block_size = block_size

        self.max_x_slots = (window_width // self.block_size) - 1
        self.max_y_slots = (window_height // self.block_size) - 1
        
        self.coordinates = [0, 0]
        self.spawn_new_location([])

    def spawn_new_location(self, snake_coordinates):
        while True:
            rand_x = random.randint(0, self.max_x_slots) * self.block_size
            rand_y = random.randint(0, self.max_y_slots) * self.block_size
            
            potential_spot = [rand_x, rand_y]

            if potential_spot in snake_coordinates:
                continue
                
            self.coordinates = potential_spot
            break