class GameState:
    """
    This class is responsible for storing all the information about the current state of the chess game.
    Also responsible for determining the valid moves at the current state, and keep a move-log.
    """

    def __init__(self):
        """Describes the chessboard as a 8x8 grid where each element represents a position
        Prefix of w represents a white piece, a b represents a black piece and a -- an empty position
        Piece notation is using standard chess notation
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):
        """"""
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move

    def undo(self):
        """"""
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    def valid_moves(self):
        """"""
        return self.possible_moves()

    def possible_moves(self):
        """"""
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                ref = self.board[r][c]
                color = ref[0]
                if (color == "w" and self.white_to_move) or (color == "b" and not self.white_to_move):
                    piece = ref[1]
                    if piece == "p":
                        self.generate_pawn_moves(r, c, moves)
                    elif piece == "R":
                        self.generate_rook_moves(r, c, moves)
                    elif piece == "B":
                        self.generate_bishop_moves(r, c, moves)
                    elif piece == "N":
                        self.generate_knight_moves(r, c, moves)
                    elif piece == "K":
                        self.generate_king_moves(r, c, moves)
                    elif piece == "Q":
                        self.generate_queen_moves(r, c, moves)
        return moves

    def generate_pawn_moves(self, r, c, moves):
        """"""
        prefix = "b" if self.white_to_move else "w"
        change = -1 if self.white_to_move else +1
        start_row = 6 if self.white_to_move else 1
        if self.board[r + change][c] == "--":
            moves.append(Move((r, c), (r + change, c), self.board))
            if r == start_row and self.board[r + (change * 2)][c] == "--":
                moves.append(Move((r, c), (r + (change * 2), c), self.board))
        if c - 1 >= 0 and c + 1 <= 7:
            if self.board[r + change][c - 1][0] == prefix:
                moves.append(Move((r, c), (r + change, c - 1), self.board))
            if self.board[r + change][c + 1][0] == prefix:
                moves.append(Move((r, c), (r + change, c + 1), self.board))

    def generate_knight_moves(self, r, c, moves):
        """"""
        same_color = "w" if self.white_to_move else "b"
        deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

        def valid_position(move):
            return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

        potential_moves = map(lambda delta: (r + delta[0], c + delta[1]), deltas)
        results = filter(valid_position, potential_moves)
        for next_move in results:
            moves.append(Move((r, c), next_move, self.board))

    def generate_bishop_moves(self, r, c, moves):
        """"""
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

        def valid_position(move):
            return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while valid_position(next_move) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])

    def generate_king_moves(self, r, c, moves):
        """"""
        same_color = "w" if self.white_to_move else "b"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1), (+1, 0), (0, +1), (-1, 0), (0, -1)]

        def valid_position(move):
            return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            if valid_position(next_move):
                moves.append(Move((r, c), next_move, self.board))

    def generate_queen_moves(self, r, c, moves):
        """"""
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1), (+1, 0), (0, +1), (-1, 0), (0, -1)]

        def valid_position(move):
            return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while valid_position(next_move) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])

    def generate_rook_moves(self, r, c, moves):
        """"""
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, 0), (0, +1), (-1, 0), (0, -1)]

        def valid_position(move):
            return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while valid_position(next_move) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])


class Move:
    """"""
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        """"""
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.hash_code = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    def __eq__(self, other):
        """"""
        if isinstance(other, Move):
            return self.hash_code == other.hash_code
        return False

    def get_chess_notation(self):
        """"""
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        """"""
        return self.cols_to_files[c] + self.rows_to_ranks[r]
