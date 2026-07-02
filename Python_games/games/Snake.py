from components import Serpent, Field

class Snake:
    def __init__(self, size_field):
        self.field = Field(size_field,size_field)
        self.snake = Serpent()