"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    if terminal(board):
        return EMPTY
    for x in range(3):
        for y in range(3):
            if board[x][y] == X:
                x_count += 1
            if board[x][y] == O:
                o_count += 1

    if (isOdd(x_count) and isEven(o_count)) or (isEven(x_count) and isOdd(o_count)):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board)
    if won is not None:
        return True
    
    # for x in range(3):
    #     for y in range(3):
    #         if board[x][y] != EMPTY:
    #             return False # game still in progress


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def isOdd(num):
    if num % 2 == 0:
        return False
    return True

def isEven(num):
    if num % 2 != 0:
        return False
    return True
