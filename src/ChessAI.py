import random
from typing import List
from src.ChessEngine import Move, GameState


def random_move_ai(moves: List[Move], gs: GameState) -> Move:
    move_index = random.randint(0, len(moves) - 1)
    return moves[move_index]


piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 100000
STALEMATE = 0
DEPTH = 3


def score_board(board: List[List[str]]) -> int:
    score = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                score += piece_score.get(square[1])
            elif square[0] == "b":
                score -= piece_score.get(square[1])
    return score


def min_max_ai(moves: List[Move], gs: GameState) -> Move:
    global next_move
    next_move = None
    random.shuffle(moves)
    find_min_max(moves, gs, DEPTH, gs.white_to_move)
    return next_move


def find_min_max(moves: List[Move], gs: GameState, depth: int, white_to_move: bool):
    global next_move
    if depth == 0:
        return score_board(gs.board)
    if white_to_move:
        max_score = -CHECKMATE
        for move in moves:
            gs.make_move(move)
            next_moves = gs.valid_moves()
            score = find_min_max(next_moves, gs, depth - 1, False)
            if score > max_score:
                if depth == DEPTH:
                    next_move = move
            gs.undo()
        return max_score
    else:
        max_score = CHECKMATE
        for move in moves:
            gs.make_move(move)
            next_moves = gs.valid_moves()
            score = find_min_max(next_moves, gs, depth - 1, True)
            if score < max_score:
                if depth == DEPTH:
                    next_move = move
            gs.undo()
        return max_score


def greedy_ai(moves: List[Move], gs: GameState) -> Move:
    turn_multiplier = 1 if gs.white_to_move else -1
    random.shuffle(moves)
    best_move: Move = None
    opponent_min_max_score = CHECKMATE * turn_multiplier
    for move in moves:
        gs.make_move(move)
        opponent_moves = gs.valid_moves()
        opponent_max_score = -CHECKMATE * turn_multiplier
        for opponent_move in opponent_moves:
            gs.make_move(opponent_move)
            if gs.checkmate:
                score = -CHECKMATE * turn_multiplier
            else:
                score = score_board(gs.board) * turn_multiplier
            if score > opponent_min_max_score:
                opponent_min_max_score = score
            gs.undo()
        if opponent_min_max_score > opponent_max_score:
            opponent_min_max_score = opponent_max_score
            best_move = move
        gs.undo()
    if best_move is None:
        return moves[0]
    else:
        return best_move
