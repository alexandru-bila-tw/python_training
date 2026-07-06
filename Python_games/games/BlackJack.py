from components import *

class BlackJack:
    def __init__(self):
        while True:
            try:
                num_players = int(input("Enter number of players (1-4): ".rjust(55//2)))
                if 1 <= num_players <= 4:
                    break
                print("Please enter a number between 1 and 4.".center(55))
            except ValueError:
                print("Invalid input. Please enter a number.".center(55))
        self.players = []
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ".rjust(55//2)).strip()
            if not name:
                name = f"Player {i+1}"
            self.players.append(Player(name))

        self.deck = Deck('blackjack')
        print(('The deck starts with '+ str(len(self.deck.all_cards)) + ' cards').center(55))
        self.deck.shuffle()

    def start_game(self):
        print(f'Welcome to BlackJack {self.player.name}'.center(55))
        game_on = True
        while game_on:
            player_hands = [[]]
            cpu_cards = []

            if len(self.deck.all_cards) < 10:
                self.deck = Deck('blackjack')
                self.deck.shuffle()
                print('A new deck arrived'.center(55))

            player_hands[0].append(self.deck.deal_one())
            cpu_cards.append(self.deck.deal_one())
            player_hands[0].append(self.deck.deal_one())
            cpu_cards.append(self.deck.deal_one())

            hand_statuses = []

            hand_idx = 0
            while hand_idx < len(player_hands):
                current_hand = player_hands[hand_idx]

                while True:
                    player_score = self.calculate_score(current_hand)

                    if len(player_hands) > 1:
                        print(f'--- PLAYING HAND {hand_idx + 1} OF {len(player_hands)} ---'.center(55))

                    print('\n' + 'You can see the dealer has the card:'.center(55) + f'\n{cpu_cards[0]}\n' + 'You have:'.center(55))
                    for card in current_hand:
                        print(str(card).center(55))
                    print(f'{self.player.name.upper()} has score {player_score}.'.center(55))

                    if player_score > 21:
                        print('💥 You BUSTED! 💥'.center(55))
                        hand_statuses.append('bust')
                        break

                    can_split = len(current_hand) == 2 and current_hand[0].rank == current_hand[1].rank

                    prompt = 'Do you (H)it, (S)tand, (F)orfeit'
                    if can_split:
                        prompt += ', or S(P)lit? '
                    else:
                        prompt += '? '

                    choice = input(prompt.center(55) + '\n').upper()

                    if choice in ['H', 'HIT']:
                        current_hand.append(self.deck.deal_one())
                    elif choice in ['S', 'STAND']:
                        hand_statuses.append('stand')
                        break
                    elif choice in ['F', 'FORFEIT']:
                        hand_statuses.append('forfeit')
                        break
                    elif choice in ['P', 'SPLIT'] and can_split:
                        print('--- Splitting Pair! ---'.center(55))
                        split_card = current_hand.pop()
                        new_hand = [split_card]

                        current_hand.append(self.deck.deal_one())
                        new_hand.append(self.deck.deal_one())

                        player_hands.insert(hand_idx + 1, new_hand)

                        continue
                    else:
                        print("Invalid choice, try again.".center(55))

                hand_idx += 1

            cpu_score = self.calculate_score(cpu_cards)

            if 'stand' in hand_statuses:
                print('\n' + "Dealer's Turn".center(55))
                cpu_score = self.calculate_score(cpu_cards)

                while cpu_score < 17:
                    cpu_cards.append(self.deck.deal_one())
                    cpu_score = self.calculate_score(cpu_cards)

                print('Dealer has:'.center(55))
                for card in cpu_cards:
                    print(str(card).center(55))
                print(f'Dealer final score: {cpu_score}'.center(55))
                print('\n' + ' FINAL RESULTS '.center(55, '='))
            else:
                print('\n' + ' FINAL RESULTS '.center(55, '='))
                print("Dealer doesn't need to play.".center(55))

            for idx, hand in enumerate(player_hands):
                status = hand_statuses[idx]
                hand_score = self.calculate_score(hand)

                hand_label = f"Hand {idx + 1}: " if len(player_hands) > 1 else ""

                if status == 'bust':
                    print(f'{hand_label}💥 Busted with {hand_score}. You lose! 💥'.center(55))
                elif status == 'forfeit':
                    print(f'{hand_label}Hand forfeited.'.center(55))
                else:
                    if cpu_score > 21:
                        print(f'{hand_label}🎉 Dealer busted! You win with {hand_score}! 🎉'.center(55))
                    elif hand_score > cpu_score:
                        print(f'{hand_label}🎉 You win with {hand_score} vs {cpu_score}! 🎉'.center(55))
                    elif hand_score < cpu_score:
                        print(f'{hand_label}👹 Dealer wins with {cpu_score} vs {hand_score}. 👹'.center(55))
                    else:
                        print(f'{hand_label}👔 It is a tie at {hand_score}! 👔'.center(55))

            print('\n' + '-'*55)
            go_on = input("Do you want to play another hand? (Y/N): ".center(55) + '\n').upper()
            if go_on != 'Y':
                game_on = False
                print('Thanks for playing, Bye!'.center(55))


    def calculate_score(self, hand):
        score = sum(card.value for card in hand)

        aces = sum(1 for card in hand if card.rank == 'Ace')

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score