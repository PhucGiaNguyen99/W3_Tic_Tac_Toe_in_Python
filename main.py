"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import math

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10000  # Number of trials to run
SCORE_CURRENT = 0  # Score for squares played by the current player
SCORE_OTHER = 0  # Score for squares played by the other player

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3
DRAW = 4

# Map for constants and strings
CONSTANTS_STRING_MAP = {EMPTY: " ", PLAYERX: "X", PLAYERO: "O"}


# Add your functions here.


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
def print_name():
    print("Phuc")


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


if __name__ == '__main__':
    game = TTTBoard(5, False, None)
    game.board[1][1] = 2
    game.board[0][4] = 2

    print(game.__str__())
    # print("Rows: ")
    # print(game.get_rows(game.board))
    # print("Cols: ")
    # print(game.get_cols(game.board))
    print("lines: ")
    print(game.get_lines(game.board))
    l = [1, 1, 2, 3, 3, 3]
    print(set(l))
    # print(game.get_empty_squares())
    # game.move(1, 1, PLAYERO)
    # game.move(1, 2, PLAYERX)

    # print(game.__str__())
