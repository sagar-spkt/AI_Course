import copy
import random


class TicTacToeGame:
    def __init__(self, board=None, player='X'):
        if board is None:
            board = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ']
        self.board = board
        self.current_player = player

    @property
    def next_player(self):
        return 'O' if self.current_player == 'X' else 'X'

    def show(self):
        print("""
                {} | {} | {}
                ------------
                {} | {} | {}
                ------------
                {} | {} | {}
                """.format(*self.board))

    def terminates(self):
        if self.winner() in ['X', 'O']:
            return True
        for i in self.board:
            if i == ' ':
                return False
        return True  # draw

    def winner(self):
        winning_configs = [[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8],
                           [0, 3, 6],
                           [1, 4, 7],
                           [2, 5, 8],
                           [0, 4, 8],
                           [6, 4, 2]]
        for player in (self.current_player, self.next_player):
            player_positions = self.get_player_positions(player)
            for winning_config in winning_configs:
                win = True
                for positions in winning_config:
                    if positions not in player_positions:
                        win = False
                        break
                if win:
                    return player
        return 'Nobody'

    def get_player_positions(self, player):
        positions = []
        for i in range(len(self.board)):
            if self.board[i] == player:
                positions.append(i)
        return positions

    def available_positions(self):
        """
        gives available positions
        :return: positions list
        """
        positions = []
        for i in range(0, len(self.board)):
            if self.board[i] == ' ':
                positions.append(i)
        return positions

    def get_successors(self):
        if self.terminates():
            return None
        next_game_state = []
        for position in self.available_positions():
            next_state = copy.deepcopy(self)
            next_state.board[position] = self.current_player
            next_state.current_player = self.next_player
            next_game_state.append(next_state)
        return next_game_state

    def get_utility(self):
        if self.winner() == 'X':
            return 1
        elif self.winner() == 'O':
            return 0
        return 0.5

    def place_tic_tac_toe(self, state):
        self.board = state.board
        self.current_player = state.current_player


class MiniMaxAlgo:
    def __init__(self, game_node: TicTacToeGame):
        self.game_node = game_node

    def search_best_move(self):
        draw_value = self.game_node.get_utility()
        successors = self.game_node.get_successors()
        best_successors = []
        for successor in successors:
            if self.game_node.current_player == 'X':
                value = self.min_value(successor)
                if value > draw_value:
                    best_successors = [successor]
                elif value == draw_value:
                    best_successors.append(successor)
            elif self.game_node.current_player == 'O':
                value = self.max_value(successor)
                if value < draw_value:
                    best_successors = [successor]
                elif value == draw_value:
                    best_successors.append(successor)
        return best_successors if best_successors else successors

    def max_value(self, state):
        if state.terminates():
            return state.get_utility()
        best_value = float('-inf')
        successors = state.get_successors()
        for successor in successors:
            best_value = max(best_value, self.min_value(successor))
        return best_value

    def min_value(self, state):
        if state.terminates():
            return state.get_utility()
        best_value = float('inf')
        successors = state.get_successors()
        for successor in successors:
            best_value = min(best_value, self.max_value(successor))
        return best_value


if __name__ == '__main__':
    print("Doesn't work well")
    tic_tac_toe = TicTacToeGame()
    tic_tac_toe.show()

    while not tic_tac_toe.terminates():
        minimax = MiniMaxAlgo(tic_tac_toe)
        best_states = minimax.search_best_move()
        tic_tac_toe.place_tic_tac_toe(random.choice(best_states))
        tic_tac_toe.show()

        if tic_tac_toe.terminates():
            break

        minimax = MiniMaxAlgo(tic_tac_toe)
        best_states = minimax.search_best_move()
        tic_tac_toe.place_tic_tac_toe(random.choice(best_states))
        tic_tac_toe.show()

    print("Game terminated. " + tic_tac_toe.winner() + " wins.")
