import time
import numpy as np
from problems import NQueen
from genetic_nqueen_adapter import NQueenGenetic

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


if __name__ == '__main__':
    board_size = int(input('Enter size of board: '))
    initial_pop_size = int(input('Enter size of initial population: '))
    t = time.time()
    try:
        solution = genetic_algorithm(NQueenGenetic.random_boards(n=initial_pop_size, size=board_size))
        if solution:
            solution.display()
        print("Heuristics value of solution: ", solution.heuristic())
    except RecursionError as err:
        print(err)
    print('Time taken: ', time.time() - t, 'sec')
