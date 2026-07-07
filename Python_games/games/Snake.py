import time
from components import Serpent, Field
from components.Field import clear_screen
import sys
import os, fcntl

orig_fl = None

def get_keypress():
    try:
        #read 1 char from nonblocking stdin
        return sys.stdin.read(1).lower()
    except IOError:
        return None

def make_stdin_non_blocking():
    #this will make stdin non-blocking.
    fd = sys.stdin.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

def restore_stdin_blocking():
    global orig_fl
    if isinstance(orig_fl, int):
        fd = sys.stdin.fileno()
        fcntl.fcntl(fd, fcntl.F_SETFL, orig_fl)

class Snake:
    def __init__(self, size_field):
        self.field = Field(size_field,size_field)
        self.snake = Serpent()

    def render_field(self):
        make_stdin_non_blocking()

        try:
            is_game_over = False
            while not is_game_over:
                key = get_keypress()
                if key:
                    self.snake.change_direction(key)

                self.snake.move()

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
                self.field.render(self.snake, (2, 2))

                time.sleep(0.5)

        finally:
            restore_stdin_blocking()