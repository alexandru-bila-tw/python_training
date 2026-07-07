import os

def clear_screen():
    #In intelij need edit configuration-> modify options -> emulate the terminal in output console
    os.system('cls' if os.name == 'nt' else 'clear')

class Field:
    def __init__(self,max_x,max_y):
        self.max_x = max_x
        self.max_y = max_y

    def render(self, serpent, food_coord=None):
        board_rows = []
        for y in range(self.max_y):
            row_chars = []
            for x in range(self.max_x):

                serpent_char = serpent.get_character_at(x, y)

                if serpent_char:
                    row_chars.append(serpent_char)
                elif food_coord and (x, y) == food_coord:
                    row_chars.append('🧇 ')

                else:
                    row_chars.append(".  ")

            board_rows.append("   ".join(row_chars))

        border = "+" + "-" * (self.max_x * 2 - 1) + "+"

        print(border)
        for row in board_rows:
            print(f"|{row}|")
        print(border)
