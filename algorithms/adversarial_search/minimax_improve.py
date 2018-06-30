from ai_problems.game import TicTacToeGame


def min_value(game_node, alpha, beta):
    if game_node.terminates():
        return game_node.get_utility()

    best_value = float('inf')
    for successor in game_node.get_successors():
        best_value = min(best_value, max_value(successor, alpha, beta))
        if best_value <= alpha:
            return best_value
        beta = min(beta, best_value)

    return best_value


def max_value(game_node, alpha, beta):
    if game_node.terminates():
        return game_node.get_utility()

    best_value = float('-inf')
    for successor in game_node.get_successors():
        best_value = max(best_value, min_value(successor, alpha, beta))
        if best_value >= beta:
            return best_value
        alpha = max(alpha, best_value)
    return best_value


def alpha_beta_pruning(root_node: TicTacToeGame):
    alpha = float('-inf')
    beta = float('inf')

    successors = root_node.get_successors()
    best_successors = []

    for successor in successors:
        if root_node.current_player == root_node.MAX:
            value = min_value(successor, alpha, beta)
            if value > alpha:
                alpha = value
                best_successors = [successor]

        elif root_node.current_player == root_node.MIN:
            value = max_value(successor, alpha, beta)
            if value < beta:
                beta = value
                best_successors = [successor]

    return best_successors if best_successors else successors
