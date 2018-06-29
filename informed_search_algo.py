from uninformed_search_algo import uniform_cost_search


def astar_search(root_node):
    def eval_func(x):
        return x.path_cost_from_root() + x.heuristic()

    def successor_generator(x):
        return x.get_near_states()

    return uniform_cost_search(root_node, eval_func=eval_func, successor_generator=successor_generator)


def hill_climbing(current_node):
    """
    Steepest-Ascent Hill Climbing
    :param current_node:
    :return: best local solution
    """
    while True:
        neighbours = current_node.get_near_states()
        if not neighbours:
            # if not any neighbours than current_node is best solution
            return current_node
        best_neighbour = min(neighbours, key=lambda node: node.heuristic())
        if best_neighbour.heuristic() >= current_node.heuristic():  # if replaced by '>' only might stuck in `flat`
            return current_node
        current_node = best_neighbour

