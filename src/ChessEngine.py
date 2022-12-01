"""
This class is responsible for storing all the information about the current state of the chess game.
Also responsible for determining the valid moves at the current state, and keep a move-log.
"""


class GameState:
    def __init__(self):
        # Describes the chessboard as a 8x8 grid where each element represents a position
        # Prefix of w represents a white piece, a b represents a black piece and a -- an empty position
        # Piece notation is using standard chess notation
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
