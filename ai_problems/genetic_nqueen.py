import random
import numpy as np
from ai_problems.search_problems import NQueen


class NQueenGenetic(NQueen):
    def __init__(self, board=None, size=None, parent=None, goal_fitness=None):
        super().__init__(board, size, parent=parent[0] if parent is not None else None)
        self.parent1 = self.parent  # NQueen parent is parent1
        self.parent2 = parent[1] if parent is not None else None
        self.goal_fitness = self.board_size*(self.board_size - 1)/2 if goal_fitness is None else goal_fitness

    # def __eq__(self, other):
    #     return np.array_equal(self.board, other.board)

    @staticmethod
    def board_from_list(list_repr: list, parent=None) -> NQueen:
        """
        should have one non-zero element in each column
        :param parent: tuple including two parents (parent1, parent2)
        :param list_repr:
        :return:
        """
        board = np.zeros((len(list_repr), len(list_repr)))
        board[list_repr, list(range(len(board)))] = 1
        return NQueenGenetic(board=board, parent=parent)

    def board_list_repr(self) -> list:
        """
        should have one non-zero element in each column
        :return:
        """
        return self.board.transpose().nonzero()[1]

    @staticmethod
    def random_boards(n, size) -> list:
        """
        return `n` numbers of random boards
        :param size: size of board
        :param n:
        :return:
        """
        return [NQueenGenetic(size=size) for _ in range(n)]

    def fitness_function(self) -> int:
        """
        :return: fitness_value: number of non-attacking pairs of queen
        """
        total_pair = self.board_size*(self.board_size - 1)/2
        return total_pair - self.heuristic()

    def termination_check(self):
        return self.goal_fitness == self.fitness_function()

    def mutate(self):
        """
        mutate itself if probability is high
        :return: mutated: if possible else itself
        """
        list_repr = self.board_list_repr()
        mutation_probability = random.uniform(0, 1)  # TODO use other distribution
        if mutation_probability < 0.7:  # TODO use best condition
            location1 = random.randint(0, self.board_size - 1)
            location2 = random.randint(0, self.board_size - 1)
            if self.board_size > 1:
                while location1 == location2:
                    location2 = random.randint(0, self.board_size - 1)
            list_repr[location1], list_repr[location2] = list_repr[location2], list_repr[location1]
        return NQueenGenetic.board_from_list(list_repr)
