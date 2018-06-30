import time
import random
import numpy as np
from problems import NQueen
from genetic_nqueen_adapter import NQueenGenetic
from game import TicTacToeGame

from uninformed_search_algo import (
    breadth_first_search,
    depth_first_search,
    depth_limit_search,
    uniform_cost_search,
)
from informed_search_algo import (
    astar_search,
    hill_climbing,
    simulated_annealing,
    genetic_algorithm,
)

from adversial_search_algo import (
    minimax_search_algo,
)


if __name__ == '__main__':
    tic_tac_toe = TicTacToeGame()
    tic_tac_toe.show()

    while not tic_tac_toe.terminates():
        success = False
        while not success:
            success = tic_tac_toe.place_in_position(int(input('Your turn, Enter position: ')))
            tic_tac_toe.show()
            if not success:
                print("Position already occupied")

        if tic_tac_toe.terminates():
            break

        print('Computer\'s turn ')
        best_next = minimax_search_algo(tic_tac_toe)
        tic_tac_toe.place_tic_tac_toe(random.choice(best_next))
        tic_tac_toe.show()

    print("Game terminated. " + tic_tac_toe.winner() + ' wins.')

