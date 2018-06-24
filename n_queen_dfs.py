import copy
import numpy as np


class State:
    def __init__(self, board):
        self.board = board
        self.board_size = len(self.board)

    def is_safe(self, row, col):
        row_elem = self.board[row, :]  # rowth elements
        col_elem = self.board[:, col]  # colth elements
        diag1_elem = self.board.diagonal(col - row)  # principle diagonal about (row, col)
        # for anti-diagonal about (row, col) flip board left-right and get principle diagonal about (row, size-1-col)
        diag2_elem = np.diagonal(np.fliplr(self.board), self.board_size - 1 - col - row)

        # if queen in any row_elem, col_elem, diag1_elem, diag2_elem
        if 1 in row_elem or 1 in col_elem or 1 in diag1_elem or 1 in diag2_elem:
            return False
        return True

    def goal_state(self):
        return np.count_nonzero(self.board) == len(self.board)  # check if all queen are placed or not


class Node:
    def __init__(self, board, parent=None):
        self.state = State(board)
        self.parent = parent


def n_queen_dfs(node, explored=None):
    if node.state.goal_state():
        return node
    else:
        if explored is None:
            explored = []
        explored.append(node)
        for i in range(node.state.board_size):
            for j in range(node.state.board_size):
                if node.state.board[i][j] != 0 or not node.state.is_safe(i, j):
                    continue

                # generate child node for the action
                child = copy.deepcopy(node)
                child.parent = node
                child.state.board[i][j] = 1

                if child.state.goal_state():
                    return child
                elif any([np.array_equal(child.state.board, elem.state.board) for elem in explored]):
                    continue
                else:
                    result_child = n_queen_dfs(child)
                    if not result_child:
                        continue
                    return result_child
    return None


size = int(input("Enter size: "))
result = n_queen_dfs(Node(np.zeros(size * size).reshape(size, size)))
print("The solution is: \n", result.state.board if result else "No solution")
