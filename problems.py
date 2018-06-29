import copy
import numpy as np
import random


class NQueen:
    def __init__(self, board=None, size=None, parent=None):
        if board is None and size is None:
            raise ValueError("At least board or size need to be given")

        if board is None:  # generate random placed nqueen board each in a column
            board = np.zeros((size, size))
            for col in range(size):
                board[:, col][random.randint(0, size-1)] = 1

        self.board = board
        self.parent = parent
        self.board_size = len(self.board)

    def path_cost_from_root(self):
        """
        Path cost for this problem is unit
        :return:
        """
        if not self.parent:
            return 0
        return self.parent.path_cost_from_root() + 1

    def heuristic(self):
        attack_counter = 0
        nonzeros = self.board.nonzero()
        for row, col in list(zip(nonzeros[0], nonzeros[1])):
            attack_counter += np.count_nonzero(self.board[:, col])
            attack_counter += np.count_nonzero(self.board[row, :])
            attack_counter += np.count_nonzero(self.board.diagonal(col - row))
            attack_counter += np.count_nonzero(np.diagonal(np.fliplr(self.board), self.board_size - 1 - col - row))
        return (attack_counter - np.count_nonzero(self.board) * 4) / 2  # remove self counting and double counting

    def display(self):
        print(self.board)

    def is_safe(self, row, col):
        """
        put queen at that place and test heuristics
        :param row:
        :param col:
        :return:
        """
        self.board[row, col] = 1
        result = False
        if self.heuristic() == 0:
            result = True
        self.board[row, col] = 0
        return result

    def goal_test(self):
        if np.count_nonzero(self.board) == self.board_size and self.heuristic() == 0:
            return True
        return False

    def is_in(self, array_list):
        return any([np.array_equal(self.board, iter_item.board) for iter_item in array_list])

    def position_in(self, array_list):
        try:
            return [np.array_equal(self.board, iter_item.board) for iter_item in array_list].index(True)
        except ValueError:
            return None

    def generate_successors(self):
        """
        used for iterative state formulation
        :return:
        """
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

    def get_near_states(self):
        """
        used for complete state formulation
        :return:
        """
        near_states_list = []
        for col in range(self.board_size):
            for row in list(np.where(self.board[:, col] == 0)[0]):
                near_state = copy.deepcopy(self)
                near_state.parent = self
                near_state.board[:, col] = np.zeros(self.board_size)
                near_state.board[row][col] = 1
                near_states_list.append(near_state)
        return near_states_list


class RouteFindingProblem:
    def __init__(self, route_file):
        pass
