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


def simulated_annealing():
    pass

