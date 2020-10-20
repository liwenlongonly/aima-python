# TODO import the necessary classes and methods
from helper import *
import sys


if __name__ == '__main__':
    input_file = sys.argv[1]

    # TODO implement
    state = game_state_input("example-input.txt")
    ttt = TicTacToePA2(state)
    print('Whose turn is it in this state?')
    # TODO: print either X or O
    print(ttt.to_move(state))
    print(
        'If both X and O play optimally from this state, does X have a guaranteed win, guaranteed loss, or guaranteed draw')
    # TODO: print one of win, loss, draw
    score = ttt.play_game(minmax_player, minmax_player)
    if "O" in ttt.to_move(state):
        score = -score
    if score > 0:
        print("win")
    elif score < 0:
        print("loss")
    else:
        print("draw")
