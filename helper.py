from games import *


def gen_state(to_move='X', x_positions=[], o_positions=[], h=3, v=3):
    """Given whose turn it is to move, the positions of X's on the board, the
    positions of O's on the board, and, (optionally) number of rows, columns
    and how many consecutive X's or O's required to win, return the corresponding
    game state"""

    moves = set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]) - set(x_positions) - set(o_positions)
    moves = list(moves)
    board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'
    return GameState(to_move=to_move, utility=0, board=board, moves=moves)

def game_state_input(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    y = 0
    x_positions = []
    o_positions = []
    to_move = "X"
    for line in lines:
        y += 1
        if not line.startswith('#'):
            rs = line.replace('\n', '')
            ar = rs.split(' ')
            while '' in ar:
                ar.remove("")
            x = 0
            for value in ar:
                x += 1
                if "X" in value:
                    x_positions.append((y, x))
                elif 'O' in value:
                    o_positions.append((y, x))
    if len(o_positions) < len(x_positions):
        to_move = "O"

    return gen_state(to_move=to_move, x_positions=x_positions, o_positions=o_positions)

class TicTacToePA2(TicTacToe):
    """Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, state=None, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        if state is None:
            moves = [(x, y) for x in range(1, h + 1)
                     for y in range(1, v + 1)]
            self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)
        else:
            self.initial = state
