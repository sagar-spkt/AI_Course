from uninformed_search_algo import uniform_cost_search


def astar_search(root_node):
    eval_func = None  # TODO add evaluation function
    return uniform_cost_search(root_node, eval_func=eval_func)
