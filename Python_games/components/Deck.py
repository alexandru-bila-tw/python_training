import random
from components import Card, suits

CARD_VALUES = {
    'standard': {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
    },
    'blackjack':{
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }
}

class Deck:

    def __init__(self, game_type='standard'):
        value_map = CARD_VALUES.get(game_type.lower(), CARD_VALUES['standard'])
        ranks = list(value_map.keys())
        self.all_cards = [
            Card(suit, rank, value_map[rank])
            for suit in suits
            for rank in ranks
        ]


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        if self.all_cards:
            return self.all_cards.pop()
        return None