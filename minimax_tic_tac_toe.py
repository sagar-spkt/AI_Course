import random  # for choosing random moves from same cost moves


class TicTacToe(object):
    def __init__(self):
        """
        Instantiate empty board
        """

        self.__board = [' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ']
        self.player = 'X'

    @property
    def next_player(self):
        return 'X' if self.player == 'O' else 'O'

    def show(self):
        print("""
        {} | {} | {}
        ------------
        {} | {} | {}
        ------------
        {} | {} | {}
        """.format(*self.__board))

    def terminates(self):
        if self.winner() in ['X', 'O']:
            return True
        for i in self.__board:
            if i == ' ':
                return False
        return True  # draw

    def get_best_positions(self):
        draw_cost = 0.5
        best_position = []  # initialize with empty list
        available_positions = self.__available_positions()
        for position in available_positions:
            self.place_tic_tac(position)  # try the move
            trial_cost = self.__minimax()
            self.remove_tic_tac(position)  # undo trial

            if trial_cost > draw_cost and self.player == 'X':
                best_position = [position]
            elif trial_cost < draw_cost and self.player == 'O':
                best_position = [position]
            elif draw_cost == trial_cost:
                best_position.append(position)

        return best_position if best_position else available_positions

    def place_tic_tac(self, position):
        """
        places players mark on position if free;
        changes player
        :param position:
        :return: true if successful
        """
        if self.__board[position] == ' ':
            self.__board[position] = self.player
            self.player = self.next_player
            return True
        return False

    def remove_tic_tac(self, position):
        self.__board[position] = ' '
        self.player = self.next_player

    def winner(self):
        winning_configs = [[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8],
                           [0, 3, 6],
                           [1, 4, 7],
                           [2, 5, 8],
                           [0, 4, 8],
                           [6, 4, 2]]
        for player in (self.player, self.next_player):
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

    def __available_positions(self):
        """
        gives available positions
        :return: positions list
        """
        positions = []
        for i in range(0, len(self.__board)):
            if self.__board[i] == ' ':
                positions.append(i)
        return positions

    def __minimax(self):
        if self.terminates():
            if self.winner() == 'X':
                return 1
            elif self.winner() == 'O':
                return 0
            elif self.winner() == 'Nobody':
                return 0.5
        if self.player == 'X':
            best_cost = 0
            for position in self.__available_positions():
                self.place_tic_tac(position)
                next_player_cost = self.__minimax()
                self.remove_tic_tac(position)
                best_cost = max(best_cost, next_player_cost)
            return best_cost
        if self.player == 'O':
            best_cost = 1
            for position in self.__available_positions():
                self.place_tic_tac(position)
                next_player_cost = self.__minimax()
                self.remove_tic_tac(position)
                best_cost = min(best_cost, next_player_cost)
            return best_cost

    def get_player_positions(self, player):
        positions = []
        for i in range(len(self.__board)):
            if self.__board[i] == player:
                positions.append(i)
        return positions


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    # show board
    tic_tac_toe.show()

    # loop until the game is over
    while not tic_tac_toe.terminates():
        # MAX's turn
        best_positions = tic_tac_toe.get_best_positions()
        print("best choices: ", best_positions)
        # tic_tac_toe.place_tic_tac(random.choice(best_positions)) # uncomment this line to make computer play
        tic_tac_toe.place_tic_tac(int(input("Enter position")))
        tic_tac_toe.show()

        # if max move terminates game, break
        if tic_tac_toe.terminates():
            break

        # MIN's turn
        best_positions = tic_tac_toe.get_best_positions()
        print("best choices: ", best_positions)
        # tic_tac_toe.place_tic_tac(random.choice(best_positions))
        tic_tac_toe.place_tic_tac(int(input("Enter position")))
        tic_tac_toe.show()

    # after game terminates show the results
    print("Game terminated." + tic_tac_toe.winner() + " wins.")
