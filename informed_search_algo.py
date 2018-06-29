import itertools
import math
import random
import copy
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


def random_selection(pop: list):
    """
    randomly select top two best parents
    :param pop:
    :return:
    """
    pop.sort(key=lambda temp: temp.fitness_function(), reverse=True)
    top_size = int(len(pop)/3) if len(pop) >= 9 else len(pop)
    try:
        return random.sample(pop[:top_size], 2)
    except ValueError:
        """
        if alone become hermaphrodite
        and believe in mutation
        otherwise give same next generation
        """
        return pop + pop


def reproduce(x, y):
    """
    x and y should be an instance of class
    which has staticmethod to create instance
    from list representation
    :param x: parent first
    :param y: parent second
    :return:
    """
    crossover = random.randint(1, x.board_size - 2)
    x_list_repr = x.board_list_repr()
    y_list_repr = y.board_list_repr()
    # why a, b = b, a swapping not working
    temp = copy.deepcopy(x_list_repr[crossover:])
    x_list_repr[crossover:] = y_list_repr[crossover:]
    y_list_repr[crossover:] = temp
    return x.__class__.board_from_list(x_list_repr, parent=(x, y)), y.__class__.board_from_list(y_list_repr, parent=(x, y))


def genetic_algorithm(population: list, limit=200):
    if population[0].board_size not in [2, 3]:  # condition only for nqueen problem otherwise remove it
        for i in range(limit):
            new_population = []

            j = 0
            while j < len(population):
                x, y = random_selection(population)
                children = reproduce(x, y)
                children = (children[0].mutate(), children[1].mutate())
                new_population += children
                j += 1

            population += new_population
            best_in_pop = population[population.index(max(population, key=lambda temp: temp.fitness_function()))]
            if best_in_pop.termination_check():
                return best_in_pop
    return population[population.index(max(population, key=lambda temp: temp.fitness_function()))]

