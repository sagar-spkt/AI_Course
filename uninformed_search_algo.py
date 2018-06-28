def breadth_first_search(root_node):
    """
    root node must have methods like
    goal_test(),
    generate_successors(),
    membership test in iterator
    :param root_node:
    :return: solution node
    """
    if root_node.goal_test():
        return root_node

    frontier = [root_node]
    explored = []

    while frontier:
        node = frontier.pop(0)
        explored.append(node)

        for successor in node.generate_successors():
            if not successor:
                continue
            if not (successor.is_in(frontier) and successor.is_in(explored)):
                if successor.goal_test():
                    return successor
                frontier.append(successor)
    return None  # No Solution


def depth_first_search(node, explored=None):
    """
    root node must have methods like
    goal_test(),
    generate_successors() => should return empty set/list if not any successors,
    membership test in iterator
    :param node:
    :param explored: previously visited nodes list
    :return: solution node
    """

    # uncomment following line to use DLS as DFS
    # return depth_limit_search(node, limit=float('inf'), explored=explored)

    if node.goal_test():
        return node
    if not explored:
        explored = []
    explored.append(node)
    for successor in node.generate_successors():
        if not successor:
            continue
        if successor.goal_test():
            return successor
        elif successor.is_in(explored):
            continue
        else:
            solution_node = depth_first_search(successor, explored)
            if solution_node:
                return solution_node
    return None  # No solution


def depth_limit_search(node, limit, explored=None):
    """
    root node must have methods like
    goal_test(),
    generate_successors(),
    membership test in iterator
    :param node:
    :param limit: maximum depth allowed
    :param explored: previously visited nodes list
    :return: solution node cutoff and solution flag
    """
    if node.goal_test():
        return {'cutoff': False, 'is_solution': True, 'solution_node': node}
    elif limit == 0:
        return {'cutoff': True, 'is_solution': False, 'solution_node': None}
    else:
        if not explored:
            explored = []
        cutoff_occurred = False
        explored.append(node)
        for successor in node.generate_successors():
            if not successor:
                continue
            if successor.is_in(explored):
                continue
            result = depth_limit_search(successor, limit-1, explored)
            if result['cutoff']:
                cutoff_occurred = True
            elif result['is_solution']:
                return result
        if cutoff_occurred:
            return {'cutoff': True, 'is_solution': False, 'solution_node': None}
        else:
            return {'cutoff': False, 'is_solution': False, 'solution_node': None}


def uniform_cost_search(root_node):
    """
    root node must have methods like
    goal_test(),
    generate_successors(),
    membership test in iterator
    :param root_node: should have property path cost from root
    :return: solution node if found else none
    """
    frontier = [root_node]
    explored = []

    while frontier:
        frontier.sort(key=lambda x: x.path_cost_from_root())
        node = frontier.pop(0)
        if node.goal_test():
            return node
        explored.append(node)
        for successor in node.generate_successors():
            if not successor:  # checks for no successor
                continue
            if not (successor.is_in(frontier) and successor.is_in(explored)):
                frontier.append(successor)
            elif successor.is_in(frontier):
                position = successor.position_in(frontier)
                if frontier[position].path_cost_from_root() > successor.path_cost_from_root():
                    frontier.pop(position)
                    frontier.append(successor)
    return None
