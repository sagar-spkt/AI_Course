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


def n_queen_dfs(node):
    if node.state.goal_state():
        return node
    else:
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
                else:
                    result = n_queen_dfs(child)
                    if not result:
                        continue
                    return result
    return None


size = int(input("Enter size: "))
print("The solution is: \n", n_queen_dfs(Node(np.zeros(size * size).reshape(size, size))).state.board)
