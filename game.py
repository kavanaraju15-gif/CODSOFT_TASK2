# Winning combinations for Tic-Tac-Toe
WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def check_winner(board):
    """
    Check whether X or O has won,
    or whether the game is a draw.
    """

    for a, b, c in WINNING_COMBINATIONS:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a]

    # If there are no empty spaces, it's a draw
    if "" not in board:
        return "Draw"

    return None


def get_available_moves(board):
    """
    Return the positions that are still empty.
    """
    return [
        i for i, value in enumerate(board)
        if value == ""
    ]


def make_move(board, position, player):
    """
    Place X or O on the selected position.
    """

    if board[position] == "":
        board[position] = player
        return True

    return False