import copy
import numpy as np


class NQueen:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.board_size = len(self.board)

    def display(self):
        print(self.board)

    def is_safe(self, row, col):
        row_elem = self.board[row, :]  # rowth elements
        col_elem = self.board[:, col]  # colth elements
        diag1_elem = self.board.diagonal(col - row)  # principle diagonal about (row, col)
        # for anti-diagonal about (row, col) flip board left-right and get principle diagonal about (row, size-1-col)
        diag2_elem = np.diagonal(np.fliplr(self.board), self.board_size - 1 - col - row)

        # if queen in any row_elem, col_elem, diag1_elem, diag2_elem: unsafe
        if 1 in row_elem or 1 in col_elem or 1 in diag1_elem or 1 in diag2_elem:
            return False
        return True

    def goal_test(self):
        if np.count_nonzero(self.board) == len(self.board):
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if self.board[i][j]:
                        self.board[i][j] = 0
                        check_result = self.is_safe(i, j)
                        self.board[i][j] = 1
                        if not check_result:
                            return False
            return True
        return False

    def is_in(self, array_list):
        return any([np.array_equal(self.board, iter_item.board) for iter_item in array_list])

    def generate_successors(self):
        successors = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] != 0 or not self.is_safe(i, j):
                    continue
                child = copy.deepcopy(self)
                child.parent = self
                child.board[i][j] = 1
                successors.append(child)
        return successors
