from collections import deque


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = deque()

    def remove_one(self):
        return self.all_cards.popleft()

    def add_cards(self,new_cards):
        if isinstance(new_cards,list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'.center(55)
