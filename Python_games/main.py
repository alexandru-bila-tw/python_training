from games import *
from games import Snake

if __name__ == '__main__':
    game_title = input('What game do you want to play? (war,blackjack,snake) ').strip().lower()
    if game_title == 'war':
        player1 = input('Username of player 1:')
        player2 = input('Username of player 2:')
        game = War(player1,player2)
        game.start_game()
    elif game_title == 'blackjack':
        game = BlackJack()
        game.start_game()
    elif game_title == 'snake':
        max_x = int(input('How wide do you want the field? (for rendering reasons for now keep 5-10) '))
        max_y = int(input('How high do you want the field? (for rendering reasons for now keep 5-10)'))
        game = Snake(max_x,max_y)
        game.render_field()
    else:
        print("I do not know that game, contact __ if want to add! Thank you, have a lovely day!")
