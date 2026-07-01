suits = {'Spades':'♠︎', 'Clubs':'♣︎', 'Hearts':'♥︎', 'Diamonds':'♦︎'}

class Card:

    def __init__(self,suit, rank, value):
        self.suit = suit
        self.icon = suits[suit]
        self.rank = rank
        self.value = value

    def __str__(self):
        return (self.rank + " of " + self.icon).center(55)