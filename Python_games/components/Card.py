values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
#           'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = {'Spades':'♠︎', 'Clubs':'♣︎', 'Hearts':'♥︎', 'Diamonds':'♦︎'}


class Card:
    def __init__(self,suit, rank, value):
        self.suit = suit
        self.icon = suits[suit]
        self.rank = rank
        self.value = value

    def __str__(self):
        return (self.rank + " of " + self.icon).center(55)