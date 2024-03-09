"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    possible_actions = set()
    for i in board:
        for j in board[i]:
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action

    if (new_board[i][j] == EMPTY):
        new_board[i][j] = player(new_board)
    else:
        raise Exception
    
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row == O*3:
            return O
        elif row == X*3:
            return X
    
    for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == O*3:
            return O
        elif column == X*3:
            return X

    d1 = [board[i][i] for i in range(3)]
    if d1 == O*3:
        return O
    elif d1 == X*3:
        return X
    
    d2 = [board[i][2-i] for i in range(3)]           
    if d2 == O*3:
        return O
    elif d2 == X*3:
        return X
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board)
    if won is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    

def isOdd(num):
    if num % 2 == 0:
        return False
    return True

def isEven(num):
    if num % 2 != 0:
        return False
    return True
