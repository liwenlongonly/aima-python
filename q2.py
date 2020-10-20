# TODO import the necessary classes and methods
from helper import *
import sys

class Statistics:

    def __init__(self):
        self.terminal_count = 0
        self.terminal_win = 0
        self.terminal_loss = 0
        self.terminal_draw = 0
        self.non_terminal_count = 0
        self.non_terminal_win = 0
        self.non_terminal_loss = 0
        self.non_terminal_draw = 0

def generate_tree(game, state, statistics):
    tree = {}
    if game.terminal_test(state):
        statistics.terminal_count += 1
        score = game.utility(state, "X")
        if score > 0:
            statistics.terminal_win += 1
        elif score < 0:
            statistics.terminal_loss += 1
        else:
            statistics.terminal_draw += 1
        return tree
    else:
        statistics.non_terminal_count += 1
        score = game.utility(state, "X")
        if score > 0:
            statistics.non_terminal_win += 1
        elif score < 0:
            statistics.non_terminal_loss += 1
        else:
            statistics.non_terminal_draw += 1
    available_actions = game.actions(state)
    for each_action in available_actions:
        if each_action not in tree:
            new_state = game.result(state, each_action)
            tree[each_action] = generate_tree(game, new_state, statistics)
    return tree


if __name__ == '__main__':
    input_file = sys.argv[1]

    # TODO implement
    state = game_state_input("example-input.txt")
    ttt = TicTacToePA2()
    statistics = Statistics()
    generate_tree(ttt, state, statistics)
    # Starting from this state, populate the full game tree.
    # The leaf nodes are the terminal states.
    # The terminal state is terminal if a player wins or there are no empty squares.
    # If a player wins, the state is considered terminal, even if there are still empty squares.
    # Answer the following questions for this game tree.
    print('How many terminal states are there?')
    # TODO print the answer
    print(statistics.terminal_count)
    print('In how many of those terminal states does X win?')
    # TODO print the answer
    print(statistics.terminal_win)
    print('In how many of those terminal states does X lose?')
    # TODO print the answer
    print(statistics.terminal_loss)
    print('In how many of those terminal states does X draw?')
    # TODO print the answer
    print(statistics.terminal_draw)
    print('How many non-terminal states are there?')
    # TODO print the answer
    print(statistics.non_terminal_count)
    print('In how many of those non-terminal states does X have a guranteed win?')
    # TODO print the answer
    print(statistics.non_terminal_win)
    print('In how many of those non-terminal states does X have a guranteed loss?')
    # TODO print the answer
    print(statistics.non_terminal_loss)
    print('In how many of those non-terminal states does X have a guranteed draw?')
    # TODO print the answer
    print(statistics.non_terminal_draw)

