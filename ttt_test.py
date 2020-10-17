from games import *


def game_state_input(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    list = []
    y = 0
    x_positions = []
    o_positions = []
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
                    x_positions.append((x, y))
                elif 'O' in value:
                    o_positions.append((x, y))
                
    return gen_state()

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

class TicTacToeTest(Game):
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
        """A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
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
    game_state_input("example-input.txt")

    state = gen_state(to_move='O', x_positions=[(1, 2), (3, 2)],
                      o_positions=[(2, 1), (2, 2)])
    print(state)
    ttt = TicTacToeTest(state)
    print(minmax_decision(state, ttt))
    ttt.display(state)

    print(ttt.play_game(alpha_beta_player))
