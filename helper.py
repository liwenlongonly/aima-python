from search import *


def best_first_tree_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(frontier), "paths remain in the frontier")
            return node
        for child in node.expand(problem):
            if child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

def astar_tree_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_tree_search(problem, lambda n: n.path_cost + h(n), display)


greedy_best_first_tree_search = best_first_tree_search

def uniform_cost_tree_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_tree_search(problem, lambda node: node.path_cost, display)