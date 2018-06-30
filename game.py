import copy


class TicTacToeGame:
    def __init__(self, board=None, MAX='X', MIN='O'):
        if board is None:
            board = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ']
        self.board = board
        self.MAX = MAX
        self.MIN = MIN
        self.current_player = self.MAX
        self.neutral_utility = 0.5

    @property
    def next_player(self):
        return self.MIN if self.current_player == self.MAX else self.MAX

    def show(self):
        print("""
                {} | {} | {}
                ------------
                {} | {} | {}
                ------------
                {} | {} | {}
                """.format(*self.board))

    def terminates(self):
        if self.winner() in [self.MAX, self.MIN]:
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
        for i in range(len(self.board)):
            if self.board[i] == ' ':
                positions.append(i)
        return positions

    def get_successors(self):
        next_game_state = []
        for position in self.available_positions():
            next_state = copy.deepcopy(self)
            next_state.board[position] = self.current_player
            next_state.current_player = self.next_player
            next_game_state.append(next_state)
        return next_game_state

    def get_utility(self):
        if self.winner() == self.MAX:
            return 1
        elif self.winner() == self.MIN:
            return 0
        return 0.5

    def place_tic_tac_toe(self, state):
        self.board = state.board
        self.current_player = state.current_player

    def place_in_position(self, position):
        """
        places players mark on position if free;
        changes player
        :param position:
        :return: true if successful
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = self.next_player
            return True
        return False
