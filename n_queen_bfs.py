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


size = int(input("Enter size: "))

# initial board
init_board = np.zeros(size * size).reshape(size, size)

# create root node
root_node = Node(init_board)

# check if root_node is goal
if root_node.state.goal_state():
    print("Solution found. Solution is: ")
    print(root_node.state.board)
    exit(0)

frontier = [root_node]
explored = []

while frontier:
    node = frontier.pop(0)
    explored.append(node)

    for i in range(size):
        for j in range(size):
            if node.state.board[i][j] != 0 or not node.state.is_safe(i, j):  # choosing action
                continue

            # generate child node for the action
            child = copy.deepcopy(node)
            child.parent = node
            child.state.board[i][j] = 1

            # as python works all in reference but we need to compare board values
            # of child node and board configuration in frontier and explored
            if not any([np.array_equal(child.state.board, elem.state.board) for elem in frontier]) \
                    or not any([np.array_equal(child.state.board, elem.state.board) for elem in explored]):
                if child.state.goal_state():
                    print("Solution found. Solution is: ")
                    print(child.state.board)
                    exit(0)
                frontier.append(child)


print("Solution not found!!")
exit(0)
