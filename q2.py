# TODO import the necessary classes and methods
from helper import *
import sys


if __name__ == '__main__':
    input_file = sys.argv[1]

    # TODO implement
    state = game_state_input("example-input.txt")
    ttt = TicTacToePA2(state)
    minmax_decision(state, ttt)
    # Starting from this state, populate the full game tree.
    # The leaf nodes are the terminal states.
    # The terminal state is terminal if a player wins or there are no empty squares.
    # If a player wins, the state is considered terminal, even if there are still empty squares.
    # Answer the following questions for this game tree.
    print('How many terminal states are there?')
    # TODO print the answer
    print(ttt.terminal_count)
    print('In how many of those terminal states does X win?')
    # TODO print the answer
    print(ttt.terminal_win)
    print('In how many of those terminal states does X lose?')
    # TODO print the answer
    print(ttt.terminal_loss)
    print('In how many of those terminal states does X draw?')
    # TODO print the answer
    print(ttt.terminal_draw)
    print('How many non-terminal states are there?')
    # TODO print the answer
    print(ttt.non_terminal_count+1)
    print('In how many of those non-terminal states does X have a guranteed win?')
    # TODO print the answer
    print(ttt.non_terminal_win)
    print('In how many of those non-terminal states does X have a guranteed loss?')
    # TODO print the answer
    print(ttt.non_terminal_loss)
    print('In how many of those non-terminal states does X have a guranteed draw?')
    # TODO print the answer
    print(ttt.non_terminal_draw)

