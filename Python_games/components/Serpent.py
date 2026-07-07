class Serpent:
    def __init__(self):
        self.coordinates = [(0, 1), (0, 0)]
        self.direction = "RIGHT"

        self.head_skin = '🐸 '
        self.body_skin = '🤌 '

    @property
    def head(self):
        return self.coordinates[0]

    @property
    def tail(self):
        return self.coordinates[-1]

    @property
    def body(self):
        return self.coordinates[1:]

    def get_character_at(self, x, y):
        if (x, y) == self.head:
            return self.head_skin
        elif (x, y) in self.body:
            return self.body_skin
        return None

    def move(self):
        #head_x,head_y
        hx, hy = self.head
        new_head = None

        if self.direction == "UP":    new_head = (hx, hy - 1)
        elif self.direction == "DOWN":  new_head = (hx, hy + 1)
        elif self.direction == "LEFT":  new_head = (hx - 1, hy)
        elif self.direction == "RIGHT": new_head = (hx + 1, hy)

        self.coordinates.insert(0, new_head)

        self.coordinates.pop()

    def change_direction(self, key):
        key_mapping = {
            'w': 'UP',
            's': 'DOWN',
            'a': 'LEFT',
            'd': 'RIGHT'
        }

        if key not in key_mapping:
            return  # Ignore irrelevant keys

        new_dir = key_mapping[key]

        # Block immediate 180-degree turnabouts
        if (new_dir == 'UP' and self.direction == 'DOWN') or \
                (new_dir == 'DOWN' and self.direction == 'UP') or \
                (new_dir == 'LEFT' and self.direction == 'RIGHT') or \
                (new_dir == 'RIGHT' and self.direction == 'LEFT'):
            return

        self.direction = new_dir