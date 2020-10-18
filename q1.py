# TODO import the necessary classes and methods
from games import *
import sys


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

class TicTacToePA2(Game):
    """Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, state=None, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        self.terminal_count = 0
        self.terminal_win = 0
        self.terminal_loss = 0
        self.terminal_draw = 0
        self.non_terminal_count = 0
        self.non_terminal_win = 0
        self.non_terminal_loss = 0
        self.non_terminal_draw = 0
        if state is None:
            moves = [(x, y) for x in range(1, h + 1)
                     for y in range(1, v + 1)]
            self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)
        else:
            self.initial = state

    def actions(self, state):
        """Legal moves are any square not yet taken."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        terminal = state.utility != 0 or len(state.moves) == 0
        """A state is terminal if it is won or there are no empty squares."""
        if terminal:
            self.terminal_count += 1
            score = self.utility(state, "X")
            if score > 0:
                self.terminal_win += 1
            elif score < 0:
                self.terminal_loss += 1
            else:
                self.terminal_draw += 1
        else:
            self.non_terminal_count += 1
            score = self.utility(state, "X")
            if score > 0:
                self.non_terminal_win += 1
            elif score < 0:
                self.non_terminal_loss += 1
            else:
                self.non_terminal_draw += 1
        return terminal

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '-'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k


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
