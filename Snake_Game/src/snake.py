class Snake:
    def __init__(self, block_size=20):
        self.block_size = block_size

        self.direction = [self.block_size, 0]

        self.coordinates = [
            [self.block_size * 5, self.block_size * 5],  # Head
            [self.block_size * 4, self.block_size * 5],  # Body
            [self.block_size * 3, self.block_size * 5]   # Tail
        ]

    def change_direction(self, new_direction):
        if (new_direction[0] == -self.direction[0]) or (new_direction[1] == -self.direction[1]):
            return False  
            
        self.direction = new_direction
        return True

    def move(self):
        head_x, head_y = self.coordinates[0]

        new_head = [head_x + self.direction[0], head_y + self.direction[1]]

        self.coordinates.insert(0, new_head)

        self.coordinates.pop()

    def grow(self):
        tail_segment = self.coordinates[-1]
        self.coordinates.append(list(tail_segment))