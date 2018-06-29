import itertools
import math
import random
from uninformed_search_algo import uniform_cost_search


def astar_search(root_node):
    def eval_func(x):
        return x.path_cost_from_root() + x.heuristic()

    def successor_generator(x):
        return x.get_near_states()

    return uniform_cost_search(root_node, eval_func=eval_func, successor_generator=successor_generator)


def hill_climbing(current_node, maximization=False):
    """
    Steepest-Ascent Hill Climbing
    :param current_node:
    :param maximization: choices between optimization defaults minimization
    :return: best local solution
    """
    if maximization:
        def best_neighbour_selector(iterator):
            return max(iterator, key=lambda node: node.heuristic())

        def break_condition(best_neigh, current):
            return best_neigh.heuristic() <= current.heuristic()
    else:
        def best_neighbour_selector(iterator):
            return min(iterator, key=lambda node: node.heuristic())

        def break_condition(best_neigh, current):
            return best_neigh.heuristic() >= current.heuristic()

    # Algorithm starts here
    while True:
        neighbours = current_node.get_near_states()
        if not neighbours:
            # if not any neighbours than current_node is best solution
            return current_node
        best_neighbour = best_neighbour_selector(neighbours)
        if break_condition(best_neighbour, current_node):
            return current_node
        current_node = best_neighbour


def exp_schedule(k=4, alpha=0.001, limit=20000):
    """
    Possible Scheduling functions:
    T(t) = 1/1+math.log(t)
    T(t) = 2 *(1-1/(1+math.exp(-t*0.001)))
    T(t) = 1/(math.log(2+t) * t*t*t)
    T(t) = 1-(1/(1+t))
    T(t) = 1/1+math.log(t)
    """
    return lambda t: (k * math.exp(-alpha * t) if t < limit else 0)
    # return lambda t: 1/(1 + math.log(t+1))


def simulated_annealing(current_node, maximization=False, schedule=exp_schedule()):
    if maximization:
        def delta_heuristic(node1, node2):
            """
            :param node1: current node
            :param node2: next node
            :return:
            """
            return node2.heuristic() - node1.heuristic()
    else:
        def delta_heuristic(node1, node2):
            return node1.heuristic() - node2.heuristic()
    for t in itertools.count():
        temp = schedule(t)
        if temp == 0 or current_node.goal_test():
            return current_node
        next_node = random.choice(current_node.get_near_states())
        delta_e = delta_heuristic(current_node, next_node)
        if delta_e > 0:
            current_node = next_node
        elif math.exp(delta_e / temp) < random.uniform(0, 1):
            current_node = next_node
