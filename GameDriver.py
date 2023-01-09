import random

# Constants
from main import TTTBoard

EMPTY = 1
PLAYERX = 2
PLAYERO = 3
DRAW = 4
NTRIALS = 10000  # Number of trials to run
SCORE_CURRENT = 0  # Score for squares played by the current player
SCORE_OTHER = 0  # Score for squares played by the other player

# Map for constants and strings
CONSTANTS_STRING_MAP = {EMPTY: " ", PLAYERX: "X", PLAYERO: "O"}


class GameDriver:
    class TTTBoard:
        """
        Class to represent a Tic-Tac-Toe board.
        """

        def __init__(self, dim, reverse=False, board=None):
            """
            Initialize the TTTBoard object with the given dimension and
            whether or not the game should be reversed.
            """
            self.dim = dim
            # Boolean for whether the game play in reverse mode or not
            self.reverse = reverse

            # Store numbers in the board. If you need to get the string of any element, get it from the map
            if board == None:
                self.board = [[EMPTY for i in range(self.dim)] for j in range(self.dim)]
            else:
                # Given a board, copy it
                self.board = [[board[row][col] for col in range(dim)] for row in range(dim)]

            # Boolean to control whether the game is drawn
            self.drawn_game = False

        def __str__(self):
            """
            Human readable representation of the board.
            """
            board_str = ""
            for row in range(self.dim):
                for col in range(self.dim):
                    board_str += CONSTANTS_STRING_MAP[self.board[row][col]]
                    if col == self.dim - 1:
                        board_str += "\n"
                    else:
                        board_str += " | "
                if row != self.dim - 1:
                    board_str += "-" * (4 * self.dim - 3)
                    board_str += "\n"
            return board_str

        def get_dim(self):
            """
            Return the dimension of the board.
            """
            return self.dim

        def square(self, row, col):
            """
            Returns one of the three constants EMPTY, PLAYERX, or PLAYERO
            that correspond to the contents of the board at position (row, col).
            """
            return self.board[row][col]

        def get_empty_squares(self):
            """
            Return a list of (row, col) tuples for all empty squares
            """
            empty_squares = []
            for row in range(self.dim):
                for col in range(self.dim):
                    if (self.square(row, col) == EMPTY):
                        empty_squares.append((row, col))
            return empty_squares

        def move(self, row, col, player):
            """
            Place player on the board at position (row, col).
            player should be either the constant PLAYERX or PLAYERO.
            Does nothing if board square is not empty.
            """
            if self.square(row, col) == EMPTY:
                self.board[row][col] = player

        def get_rows(self, board):
            return board

        def get_cols(self, board):
            result = []
            for col in range(self.dim):
                temp = []
                for row in range(self.dim):
                    temp.append(board[row][col])
                result.append(temp)
            return result

        def get_diags(self, board):
            result = []
            diag1 = []
            diag2 = []
            for i in range(self.dim):
                diag1.append(board[i][i])
                diag2.append(board[i][self.dim - 1 - i])
            result.append(diag1)
            result.append(diag2)
            return result

        def get_lines(self, board):
            lines = []
            lines.extend(self.get_rows(board))
            lines.extend(self.get_cols(board))
            lines.extend(self.get_diags(board))
            return lines

        def check_win(self):
            """
            Returns a constant associated with the state of the game
                If PLAYERX wins, returns PLAYERX.
                If PLAYERO wins, returns PLAYERO.
                If game is drawn, returns DRAW.
                If game is in progress, returns None.
            """
            # DO NOT MODIFY THE BOARD, so used a clone board
            board = self.board
            dim = self.dim
            lines = self.get_lines(board)

            for line in lines:
                if len(set(line)) == 1 and line[0] != EMPTY:
                    if self.reverse:
                        return self.switch_player(line[0])
                    else:
                        return line[0]

            # If the empty list is empty, then the game is done
            if len(self.get_empty_squares()) == 0:
                return DRAW

            # Otherwise, the game is still in progress
            return None

        def clone(self):
            """
            Return a copy of the board.
            """
            return TTTBoard(self.dim, self.reverse, self.board)

        def switch_player(self, player):
            """
            Switch the current player to the opponent.
            """
            if player == PLAYERX:
                player = PLAYERO
            else:
                player = PLAYERX

    def mc_trial(self, board: TTTBoard, player):
        '''
            This function takes a current board and the next player to move.
            The function should play a game starting with the given player by making random moves,
            alternating between players.
             The function should return when the game is over.
            The modified board will contain the state of the game, so the function does not return anything.
            In other words, the function should modify the board input.
            '''
        winner = None

        while random == None:
            # Choose a random square from the list of empty squares
            random_square = random.choice(board.get_empty_squares())
            # Set the player to the chosen random square
            board.move(random_square[0], random_square[1], player)
            # Check if there is any winner determined. The game continues only if it returns None
            winner = board.check_win()
            # Switch current player
            player = board.switch_player(player)

    def mc_update_scores(self, scores, board: TTTBoard, player):
        '''
            This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board
             a board from a completed game, and which player the machine player is.
            The function should score the completed board and update the scores grid.
            As the function updates the scores grid directly, it does not return anything,
            '''
        # After mc_trial, we know there are 3 cases: the winner is "X", the winner is "Y" or the game is Tie.

        winner = board.check_win()

        # 1. If the result is Draw, just pass the function
        if winner == DRAW:
            pass

        # 2. If computer wins, increment all computer's moves and decrement all your component's moves
        elif winner == player:
            for row in range(board.get_dim()):
                for col in range(board.get_dim()):
                    current_square = board.square(row, col)
                    if current_square == player:
                        current_square += SCORE_CURRENT
                    elif current_square != EMPTY and current_square != player:
                        current_square -= SCORE_OTHER

        # 3. If the player wins, increment all player's moves and decrement all computer's moves
        else:
            for row in range(board.get_dim()):
                for col in range(board.get_dim()):
                    current_square = board.square(row, col)
                    if current_square == player:
                        current_square -= SCORE_CURRENT
                    elif current_square == EMPTY:
                        pass
                    else:
                        current_square += SCORE_OTHER

    def get_best_move(self, board: TTTBoard, scores):
        '''
            This function takes a current board and a grid of scores.
            The function should find all of the empty squares with the maximum score
             and randomly return one of them as a (row, column) tuple.
             It is an error to call this function with a board that has no empty squares
            (there is no possible next move), so your function may do whatever it wants in that case.
            The case where the board is full will not be tested.
            '''

        # Based on the scores which you generated in mc_update_scores(), you can determine which square in the empty squares has the highest score.

        # If there is no empty square, skip this function
        if not board.get_empty_squares():
            pass

        # Otherwise, generate a dictionary with key is the empty square in the empty squares list and value is its score in the scores
        empty_squares_list = board.get_empty_squares()
        empty_squares_scores_dict = {}
        for square in empty_squares_list:
            empty_squares_scores_dict[square] = scores[square[0]][square[1]]

        # Find the max value in the values of the dictionary
        max_value = max(empty_squares_scores_dict.values())

        # Find all the keys corresponding to that max value
        max_scores_squares = [k for k, v in empty_squares_scores_dict.items() if v == max_value]

        # If there are more than one square with highest scores, randomly choose one
        return random.choice(max_scores_squares)

    def mc_move(self, board: TTTBoard, player, trials):
        '''
            This function takes a current board, which player the machine player is, and the number of trials to run.
            The function should use the Monte Carlo simulation described above to return
            a move for the machine player in the form of a (row, column) tuple.
            Be sure to use the other functions you have written!
            '''
        # Create an empty board for the list of empty squares
        empty_board = board.clone()

        # Create a clone board and list of scores for finding the best move according to Monte Carlo
        scores_list = []
        clone_board = board.clone()
        for line in range(board.get_dim()):
            scores_list.append([0] * board.get_dim())

        # Run for loop in the times of given trials, play the game with the function mc_trials() and keep track the scores
        # with the function update_scores(). After the loop, return the scores of all the squares as they are all empty.
        for t in range(trials):
            self.mc_trial(clone_board, player)
            self.mc_update_scores(scores_list, clone_board, player)

            # reset the clone board after each turn
            clone_board = empty_board.clone()

        # With the scores list, find the square with the highest score
        best_square = self.get_best_move(clone_board, scores_list)
        return best_square


if __name__ == '__main__':
    l = [(1, 2), (3, 4), (5, 6), 9]
    rm = random.choice(l)
    # print(rm)
    l = []
    for i in range(10):
        l.append([0] * 10)
    print(l)
