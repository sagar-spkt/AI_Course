from uninformed_search_algo import uniform_cost_search


def astar_search(root_node):
    def eval_func(x):
        return x.path_cost_from_root() + x.heuristic()

    def successor_generator(x):
        return x.get_near_states()

    return uniform_cost_search(root_node, eval_func=eval_func, successor_generator=successor_generator)
