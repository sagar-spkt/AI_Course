def min_value(game_node):
    if game_node.terminates():
        return game_node.get_utility()
    best_value = float('inf')
    for successor in game_node.get_successors():
        best_value = min(best_value, max_value(successor))
    return best_value


def max_value(game_node):
    if game_node.terminates():
        return game_node.get_utility()
    best_value = float('-inf')
    for successor in game_node.get_successors():
        best_value = max(best_value, min_value(successor))
    return best_value


def minimax_search(root_node):
    """
    returns best next node at current state
    priority:
        1. winning nodes
        2. draw nodes
        3. all nodes
    :param root_node:
    :return:
    """
    draw_value = root_node.neutral_utility
    successors = root_node.get_successors()
    best_successors = []
    draw_successors = []

    for successor in successors:
        if root_node.current_player == root_node.MAX:
            value = min_value(successor)
            if value > draw_value:
                best_successors.append(successor)
            elif value == draw_value:
                draw_successors.append(successor)

        elif root_node.current_player == root_node.MIN:
            value = max_value(successor)
            if value < draw_value:
                best_successors.append(successor)
            elif value == draw_value:
                draw_successors.append(successor)

    if best_successors:
        return best_successors
    elif draw_successors:
        return draw_successors
    return successors
