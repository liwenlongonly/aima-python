from search import *  # TODO import the necessary classes and methods
import sys
import math
from helper import *

def list_n_puzzle_input(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    list = []
    for line in lines:
        if not line.startswith('#'):
            rs = line.replace('\n', '')
            ar = rs.split(' ')
            while '' in ar:
                ar.remove("")
            for value in ar:
                list.append(int(value))
    return list


class NPuzzle(Problem):

    def __init__(self, initial):
        """ Define goal state and initialize a problem """
        # print("initial: %s" % (str(list(initial))))
        goal = list(range(len(initial)))
        # print("goal: %s" % (str(goal)))
        self.num_per = (int)(math.sqrt(len(goal)))
        super().__init__(initial, tuple(goal))

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['L', 'R', 'U', 'D']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % self.num_per == 0:
            possible_actions.remove('L')
        if index_blank_square < self.num_per:
            possible_actions.remove('U')
        if index_blank_square % self.num_per == self.num_per - 1:
            possible_actions.remove('R')
        if index_blank_square > self.num_per * (self.num_per - 1) - 1:
            possible_actions.remove('D')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'U': -self.num_per, 'D': self.num_per, 'L': -1, 'R': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':

    input_file: str = sys.argv[1]
    search_algo_str: str = sys.argv[2]

    # TODO implement
    npuzzle_problem = None
    if input_file is not None and len(input_file) > 0:
        npuzzle = list_n_puzzle_input(input_file)
        npuzzle_problem = NPuzzle(tuple(npuzzle))

    goal_node = None
    if search_algo_str == "DFTS":
        goal_node = depth_first_tree_search(npuzzle_problem)
    elif search_algo_str == "DFGS":
        goal_node = depth_first_graph_search(npuzzle_problem)
    elif search_algo_str == "BFTS":
        goal_node = breadth_first_tree_search(npuzzle_problem)
    elif search_algo_str == "BFGS":
        goal_node = breadth_first_graph_search(npuzzle_problem)
    elif search_algo_str == "UCTS":
        goal_node = uniform_cost_tree_search(npuzzle_problem)
    elif search_algo_str == "UCGS":
        goal_node = uniform_cost_search(npuzzle_problem)
    elif search_algo_str == "GBFTS":
        h = memoize(npuzzle_problem.h, 'h')
        goal_node = greedy_best_first_tree_search(npuzzle_problem, lambda n: h(n))
    elif search_algo_str == "GBFGS":
        h = memoize(npuzzle_problem.h, 'h')
        goal_node = greedy_best_first_graph_search(npuzzle_problem, lambda n: h(n))
    elif search_algo_str == "ASTS":
        goal_node = astar_tree_search(npuzzle_problem)
    elif search_algo_str == "ASGS":
        goal_node = astar_search(npuzzle_problem)
    else:
        print("No support this algo")

        # Do not change the code below.
    if goal_node is not None:
        print("Solution path", goal_node.solution())
        print("Solution cost", goal_node.path_cost)
    else:
        print("No solution was found.")
