from helper import *


def printTree(tree, depth = 0):
	#delete after you finish the homework
	if tree == None or len(tree) == 0:
		print ("\t" * depth, "-")
	else:
		for key, val in tree.items():
			print("\t" * depth, key)
			printTree(val, depth+1)


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
    state = game_state_input("example-input.txt")
    ttt = TicTacToePA2()
    ttt.display(state)
    statistics = Statistics()
    tree = generate_tree(ttt, state, statistics)
    printTree(tree)
    # print(ttt.to_move(state))
    print(state)
    print(statistics.terminal_count)
    print(statistics.terminal_win)
    print(statistics.terminal_loss)
    print(statistics.terminal_draw)
    print(statistics.non_terminal_count)
    print(statistics.non_terminal_win)
    print(statistics.non_terminal_loss)
    print(statistics.non_terminal_draw)
