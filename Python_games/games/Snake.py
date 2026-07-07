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

        for _ in range(self.field.max_x + 3):
            clear_screen()

            self.field.render(serpent,(2,2))
            hx, hy = serpent.head

            # Remember: valid coordinates are 0 to max_x - 1
            if hx < 0 or hx >= self.field.max_x or hy < 0 or hy >= self.field.max_y:
                print("💥 CRASH! You hit the wall!")
                is_game_over = True
                break

            # 3. Check for Self Collision (Biting your own body)
            if serpent.head in serpent.body:
                print("💀 OUCH! You bit your own tail!")
                is_game_over = True
                break

            serpent.move()

            time.sleep(0.5)