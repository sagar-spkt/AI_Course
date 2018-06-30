import random
from ai_problems.game import TicTacToeGame

from algorithms.adversarial_search import (
    minimax_search,
    alpha_beta_pruning,
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
        best_next = alpha_beta_pruning(tic_tac_toe)
        tic_tac_toe.place_tic_tac_toe(random.choice(best_next))
        tic_tac_toe.show()

    print("Game terminated. " + tic_tac_toe.winner() + ' wins.')

