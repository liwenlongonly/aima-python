import math

from search import *


def graph_travel_input(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    graph = {}
    target = []
    heuristic = {}
    for line in lines:
        if not line.startswith('#'):
            rs = line.replace('\n', '')
            ar = rs.split(' ')
            while '' in ar:
                ar.remove("")
            if '>' in line:
                if not ar[0] in graph.keys():
                   graph[ar[0]] = {}
                graph[ar[0]][ar[1]] = int(ar[3])
            if '<' in line:
                if not ar[1] in graph.keys():
                   graph[ar[1]] = {}
                graph[ar[1]][ar[0]] = int(ar[3])
            if len(ar) <= 2 and not ar[1].isdigit():
                target = ar
            elif len(ar) <= 2 and ar[1].isdigit():
                heuristic[ar[0]] = int(ar[1])

    travel_map = Graph(graph)
    print(graph)
    travel_map.heuristic = heuristic
    return travel_map, target


def list_npuzzle_input(file):
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
            for vlaue in ar:
                list.append(int(vlaue))
    return list


class TravelGraphProblem(GraphProblem):

    def h(self, node):
        heuristic = getattr(self.graph, 'heuristic', None)
        if heuristic:
            if type(node) is str:
                return heuristic[node]

            return heuristic[node.state]
        else:
            return np.inf


class NPuzzle(Problem):

    def __init__(self, initial):
        """ Define goal state and initialize a problem """
        print("initial: %s" % (str(list(initial))))
        goal = list(range(len(initial)))
        print("goal: %s" % (str(goal)))
        self.puzzle_size = len(goal)-1
        self.num_per = (int)(math.sqrt(len(goal)))
        super().__init__(initial, tuple(goal))

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % self.num_per == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < self.num_per:
            possible_actions.remove('UP')
        if index_blank_square % self.num_per == self.num_per - 1:
            possible_actions.remove('RIGHT')
        if index_blank_square > self.num_per * (self.num_per - 1) - 1:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -self.num_per, 'DOWN': self.num_per, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        zero_index = self.find_blank_square(state)
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        if self.puzzle_size % 2 == 0:
            row = zero_index // self.puzzle_size
            inversion += row

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


if __name__ == '__main__':
    travel_map, target = graph_travel_input("travel-input.txt")
    travel_problem = TravelGraphProblem(target[0], target[1], travel_map)
    print("target: %s" %( target ))
    goal_node = astar_search(travel_problem, display=True)
    print(goal_node.solution())
    print(goal_node.path_cost)

    # romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    # print(astar_search(romania_problem).solution())

    npuzzle = list_npuzzle_input("npuzzle-input.txt")
    npuzzle_problem = NPuzzle(tuple(npuzzle))
    goal_node = depth_first_graph_search(npuzzle_problem)
    print(goal_node.solution())
    print(goal_node.path_cost)
