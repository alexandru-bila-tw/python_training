from games import *
from games import Snake

if __name__ == '__main__':
    game_title = input('What game do you want to play? (war,blackjack) ').strip().lower()
    if game_title == 'war':
        player1 = input('Username of player 1:')
        player2 = input('Username of player 2:')
        game = War(player1,player2)
        game.start_game()
    elif game_title == 'blackjack':
        game = BlackJack()
        game.start_game()
    elif game_title == 'snake':
        game = Snake(5)
        game.render_field()