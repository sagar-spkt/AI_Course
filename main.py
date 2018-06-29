import time
import numpy as np
from problems import NQueen
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
)


if __name__ == '__main__':
    size = int(input('Enter size: '))
    t = time.time()
    try:
        solution = simulated_annealing(NQueen(size=size))
        solution.display()
        print("Heuristics value of solution: ", solution.heuristic())
    except RecursionError as err:
        print(err)
    print('Time taken: ', time.time() - t, 'sec')
