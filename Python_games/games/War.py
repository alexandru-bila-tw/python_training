from time import sleep

from components.Deck import Deck
from components.Player import Player


class War:
    def __init__(self,name1='Jack Daniel',name2 = 'Allen Walker'):
        self.player_one=Player(name1)
        self.player_two=Player(name2)
        deck = Deck()
        print(('The deck starts with '+ str(len(deck.all_cards)) + ' cards').center(55))
        deck.shuffle()

        for x in range(26):
            self.player_one.add_cards(deck.deal_one())
            self.player_two.add_cards(deck.deal_one())

    def start_game(self):
        print (self.player_one)
        print (self.player_two)
        game_on = True
        war_spoils = []

        rounds = 0

        while game_on:
            if len(self.player_one.all_cards) == 0:
                print(f"Player {self.player_two.name} has won the game!".center(55))
                game_on = False
                break
            if len(self.player_two.all_cards) == 0:
                print(f"Player {self.player_one.name} has won the game!".center(55))
                game_on = False
                break
            p1_card = self.player_one.remove_one()
            p2_card = self.player_two.remove_one()
            print(f'{self.player_one.name} has:'.center(55))
            print(p1_card)
            print(f'{self.player_two.name} has:'.center(55))
            print(p2_card)

            war_spoils.extend([p1_card, p2_card])

            if p1_card.value > p2_card.value:
                self.player_one.add_cards(war_spoils)
                print(f'{self.player_one.name} won {len(war_spoils)} cards!'.center(55))
                war_spoils.clear()

            elif p2_card.value > p1_card.value:
                self.player_two.add_cards(war_spoils)
                print(f'{self.player_two.name} won {len(war_spoils)} cards!'.center(55))
                war_spoils.clear()

            else:
                print("It is war time!!!".center(55))
                print(f'{self.player_one.name} has {len(self.player_one.all_cards)} cards left.'.center(55))
                print(f'{self.player_two.name} has {len(self.player_two.all_cards)} cards left.'.center(55))
                war_value = min(p1_card.value, len(self.player_one.all_cards), len(self.player_two.all_cards))
                print(f"Both players will offer {war_value} spoils of war".center(55))
                for _ in range(war_value -1):
                    war_spoils.append(self.player_one.remove_one())
                    war_spoils.append(self.player_two.remove_one())
            rounds += 1

            print(f"Round {rounds} has ended".center(55, '-'))
