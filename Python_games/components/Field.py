class Field:
    def __init__(self,max_x,max_y):
        self.max_x = max_x
        self.max_y = max_y

    def render(self, serpent, food_coord=None):
        board_rows = []
        for y in range(self.max_y):
            row_chars = []
            for x in range(self.max_x):

                if (x, y) == serpent.head:
                    row_chars.append('🐸')

                elif (x, y) in serpent.body:
                    row_chars.append('🤌')

                elif food_coord and (x, y) == food_coord:
                    row_chars.append('🧇')

                else:
                    row_chars.append(".")

            board_rows.append("   ".join(row_chars))

        border = "+" + "-" * (self.max_x * 2 - 1) + "+"

        print(border)
        for row in board_rows:
            print(f"|{row}|")
        print(border)
