from components import *

class BlackJack:
    def __init__(self,name):
        self.player=Player(name)
        self.deck = Deck('blackjack')
        print(('The deck starts with '+ str(len(self.deck.all_cards)) + ' cards').center(55))
        self.deck.shuffle()

    def start_game(self):
        print(f'Welcome to BlackJack {self.player.name}'.center(55))
        game_on = True
        while game_on:
            player_cards = []
            cpu_cards = []

            if len(self.deck.all_cards) < 10:
                self.deck = Deck('blackjack')
                self.deck.shuffle()
                print('A new deck arrived'.center(55))

            player_cards.append(self.deck.deal_one())
            cpu_cards.append(self.deck.deal_one())
            player_cards.append(self.deck.deal_one())
            cpu_cards.append(self.deck.deal_one())

            player_bust = False
            player_forfeit = False

            while True:
                player_score = self.calculate_score(player_cards)

                print('\n' + 'You can see the dealer has the card:'.center(55) + f'\n{cpu_cards[0]}\n' + 'You have:'.center(55))
                for card in player_cards:
                    print(str(card).center(55))
                print(f'{self.player.name.upper()} has score {player_score}.'.center(55))

                if player_score > 21:
                    print('💥 You BUSTED! 💥'.center(55))
                    player_bust = True
                    break

                choice = input('Do you (H)it, (S)tand, or (F)orfeit? '.center(55) + '\n').upper()

                if choice in ['H', 'HIT']:
                    player_cards.append(self.deck.deal_one())
                elif choice in ['S', 'STAND', 'PLAY']:
                    break
                elif choice in ['F', 'FORFEIT']:
                    player_forfeit = True
                    break
                else:
                    print("Invalid choice, try again.".center(55))

            if not player_bust and not player_forfeit:
                print('\n' + "Dealer's Turn".center(55))
                cpu_score = sum(card.value for card in cpu_cards)

                while cpu_score < 17:
                    cpu_cards.append(self.deck.deal_one())
                    cpu_score = sum(card.value for card in cpu_cards)

                print('Dealer has:'.center(55))
                for card in cpu_cards:
                    print(str(card).center(55))
                print(f'Dealer final score: {cpu_score}'.center(55))

                # --- DETERMINE WINNER ---
                if cpu_score > 21:
                    print('🎉 Dealer busted! You win! 🎉'.center(55))
                elif player_score > cpu_score:
                    print('🎉 You win! 🎉'.center(55))
                elif player_score < cpu_score:
                    print('👹 Dealer wins. 👹'.center(55))
                else:
                    print('👔 It is a tie! 👔'.center(55))

            elif player_forfeit:
                print("Hand forfeited.".center(55))

            print('\n' + '-'*55)
            go_on = input("Do you want to play another hand? (Y/N): ".center(55) + '\n').upper()
            if go_on != 'Y':
                game_on = False
                print('Thanks for playing, Bye!'.center(55))


    def calculate_score(self, hand):
        score = sum(card.value for card in hand)

        # Count how many Aces are in the current hand
        aces = sum(1 for card in hand if 'Ace' in str(card) or (hasattr(card, 'rank') and card.rank == 'Ace'))

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score