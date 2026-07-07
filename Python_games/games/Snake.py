import time
from components import Serpent, Field
from components.Field import clear_screen
import sys
import os, fcntl
import random
import termios


orig_fl = None
orig_termios = None

def get_keypress():
    try:
        char = sys.stdin.read(1)
        if char:
            return char.lower()
    except IOError:
        return None
    return None

def make_stdin_non_blocking():
    #this will make stdin non-blocking.
    global orig_fl, orig_termios
    fd = sys.stdin.fileno()

    orig_fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)

    orig_termios = termios.tcgetattr(fd)
    new_termios = termios.tcgetattr(fd)
    new_termios[3] = new_termios[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new_termios)

def restore_stdin_blocking():
    global orig_fl, orig_termios
    fd = sys.stdin.fileno()

    if isinstance(orig_termios, list):
        termios.tcsetattr(fd, termios.TCSANOW, orig_termios)

    if isinstance(orig_fl, int):
        fcntl.fcntl(fd, fcntl.F_SETFL, orig_fl)

def spawn_food(field, serpent):
    while True:
        food_x = random.randint(0, field.max_x - 1)
        food_y = random.randint(0, field.max_y - 1)
        food_pos = (food_x, food_y)

        if food_pos not in serpent.coordinates:
            return food_pos

class Snake:
    def __init__(self, max_x,max_y):
        self.field = Field(max_x,max_y)
        self.snake = Serpent()

    def render_field(self):
        make_stdin_non_blocking()

        food_pos = spawn_food(self.field, self.snake)
        score = 0

        try:
            is_game_over = False
            while not is_game_over:
                key = get_keypress()
                if key:
                    self.snake.change_direction(key)

                ate_food = (self.snake.head == food_pos)

                self.snake.move(ate_food)

                if ate_food:
                    score += 1
                    food_pos = spawn_food(self.field, self.snake)

                hx, hy = self.snake.head
                if hx < 0 or hx >= self.field.max_x or hy < 0 or hy >= self.field.max_y:
                    print("💥 CRASH! You hit the wall!")
                    is_game_over = True
                    break

                if self.snake.head in self.snake.body:
                    print("💀 OUCH! You bit your own tail!")
                    is_game_over = True
                    break

                clear_screen()
                self.field.render(self.snake, food_pos)

                time.sleep(0.5)

        finally:
            restore_stdin_blocking()