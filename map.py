from search import *  # TODO import the necessary classes and methods
import sys
from helper import *


def graph_travel_input(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    graph: dict = {}
    goal: list = []
    heuristic: dict = {}

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
                goal = ar
            elif len(ar) <= 2 and ar[1].isdigit():
                heuristic[ar[0]] = int(ar[1])

    travel_graph = Graph(graph)
    travel_graph.heuristic = heuristic
    # print("initial: %s" % (str(graph)))
    # print("goal: %s" % (str(goal)))
    return travel_graph, goal


class TravelGraphProblem(GraphProblem):

    def value(self, state):
        pass

    def h(self, node):
        heuristic = getattr(self.graph, 'heuristic', None)
        if heuristic:
            if type(node) is str:
                return heuristic[node]

            return heuristic[node.state]
        else:
            return np.inf


if __name__ == '__main__':

    input_file: str = sys.argv[1]
    search_algo_str: str = sys.argv[2]

    # TODO implement
    travel_problem = None
    if input_file is not None and len(input_file) > 0:
        travel_map, target = graph_travel_input(input_file)
        travel_problem = TravelGraphProblem(target[0], target[1], travel_map)

    goal_node = None
    if search_algo_str == "DFTS":
        goal_node = depth_first_tree_search(travel_problem)
    elif search_algo_str == "DFGS":
        goal_node = depth_first_graph_search(travel_problem)
    elif search_algo_str == "BFTS":
        goal_node = breadth_first_tree_search(travel_problem)
    elif search_algo_str == "BFGS":
        goal_node = breadth_first_graph_search(travel_problem)
    elif search_algo_str == "UCTS":
        goal_node = uniform_cost_tree_search(travel_problem)
    elif search_algo_str == "UCGS":
        goal_node = uniform_cost_search(travel_problem)
    elif search_algo_str == "GBFTS":
        h = memoize(travel_problem.h, 'h')
        goal_node = greedy_best_first_tree_search(travel_problem, lambda n: h(n))
    elif search_algo_str == "GBFGS":
        h = memoize(travel_problem.h, 'h')
        goal_node = greedy_best_first_graph_search(travel_problem, lambda n: h(n))
    elif search_algo_str == "ASTS":
        goal_node = astar_tree_search(travel_problem)
    elif search_algo_str == "ASGS":
        goal_node = astar_search(travel_problem)
    else:
        print("No support this algo")

    # Do not change the code below.
    if goal_node is not None:
        print("Solution path", goal_node.solution())
        print("Solution cost", goal_node.path_cost)
    else:
        print("No solution was found.")
