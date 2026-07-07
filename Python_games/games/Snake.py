import time
from components import Serpent, Field
from components.Field import clear_screen

class Snake:
    def __init__(self, size_field):
        self.field = Field(size_field,size_field)
        self.snake = Serpent()
    def render_field(self):
        self.field.render(self.snake,(2,2))
        serpent = Serpent()

        for _ in range(self.field.max_x):
            clear_screen()

            self.field.render(serpent,(2,2))

            serpent.move()

            time.sleep(0.5)