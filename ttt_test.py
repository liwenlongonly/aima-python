from helper import *


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
        return tree, score

    available_actions = game.actions(state)
    score = 0
    to_move = game.to_move(state)
    if to_move in "X":
        score = -1
    else:
        score = 1
    for each_action in available_actions:
        if each_action not in tree:
            new_state = game.result(state, each_action)
            tree1, score1 = generate_tree(game, new_state, statistics)
            tree[each_action] = tree1
            if to_move in "X":
                if score < score1:
                    score = score1
            else:
                if score > score1:
                    score = score1

    statistics.non_terminal_count += 1
    if score > 0:
        statistics.non_terminal_win += 1
    elif score < 0:
        statistics.non_terminal_loss += 1
    else:
        statistics.non_terminal_draw += 1
    return tree, score


if __name__ == '__main__':
    grame_state = game_state_input("example-input.txt")
    ttt = TicTacToePA2()
    ttt.display(grame_state)
    statis = Statistics()
    generate_tree(ttt, grame_state, statis)
    print(statis.terminal_count)
    print(statis.terminal_win)
    print(statis.terminal_loss)
    print(statis.terminal_draw)
    print(statis.non_terminal_count)
    print(statis.non_terminal_win)
    print(statis.non_terminal_loss)
    print(statis.non_terminal_draw)
