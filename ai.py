import random

from game import check_winner, get_available_moves


def minimax(board, depth, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for move in get_available_moves(board):
            board[move] = "O"

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[move] = ""

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in get_available_moves(board):
            board[move] = "X"

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[move] = ""

            best_score = min(best_score, score)

        return best_score


def find_best_move(board):
    """Find the best move using Minimax."""

    best_score = float("-inf")
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"

        score = minimax(
            board,
            0,
            False
        )

        board[move] = ""

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def find_random_move(board):
    """Choose a random available move."""

    available_moves = get_available_moves(board)

    if available_moves:
        return random.choice(available_moves)

    return None


def find_medium_move(board):
    """
    Medium difficulty:
    70% smart move, 30% random move.
    """

    available_moves = get_available_moves(board)

    if not available_moves:
        return None

    if random.random() < 0.7:
        return find_best_move(board)

    return random.choice(available_moves)


def find_move(board, difficulty):
    """
    Select an AI move based on difficulty.
    """

    if difficulty == "Easy":
        return find_random_move(board)

    elif difficulty == "Medium":
        return find_medium_move(board)

    else:
        return find_best_move(board)