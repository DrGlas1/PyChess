from typing import List, Tuple
from typing import Dict
from typing import Any

STARTING_BOARD = (
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
)

VALID_PIECES = ["Q", "R", "B", "K"]


class Move:
    """
    Class representing a move.

    :param self.ranks_to_rows: Converts programming notation to chess notation for rows
    :type self.ranks_to_rows: Dict[str, int]
    :param self.rows_to_ranks: Converts chess notation to programming notation for rows
    :type self.rows_to_ranks: Dict[int, str]
    :param self.files_to_cols: Converts programming notation to chess notation for cols
    :type self.files_to_cols: Dict[str, int]
    :param self.cols_to_files: Converts chess notation to programming notation for cols
    :type self.cols_to_files: Dict[int, str]
    :param self.start_row: Represents the starting row of the move
    :type self.start_row: int
    :param self.start_col: Represents the starting column of the move
    :type self.start_col: int
    :param self.end_row: Represents the ending row of the move
    :type self.end_row: int
    :param self.end_col: Represents the ending column of the move
    :type self.end_col: int
    :param self.piece_moved: String representing the piece moved
    :type self.piece_moved: str
    :param self.piece_captured: String representing the piece that the move overrides
    :type self.piece_captured: str
    :param self.hash_code: Int representing an id for determining if two moves are equivalent
    :type self.hash_code: int
    """
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        """
        Creates a move instance

        :param start_sq: The initial square of the piece being moved
        :type start_sq: tuple[int, int]
        :param end_sq: The ending square of the piece being moved
        :type: end_sq: tuple[int, int]
        :param board: The board that we move our pieces on
        :type board: List[List[str]]
        """
        self.start_row: int = start_sq[0]
        self.start_col: int = start_sq[1]
        self.end_row: int = end_sq[0]
        self.end_col: int = end_sq[1]
        self.piece_moved: str = board[self.start_row][self.start_col]
        self.piece_captured: str = board[self.end_row][self.end_col]
        self.en_passent: tuple[bool, tuple[int, int]] = (False, (0, 0))
        self.captured_en_passent: tuple[bool, tuple[int, int]] = (False, (0, 0))
        self.pawn_promotion: bool = self.piece_moved[1] == "p" and (self.end_row == 0 or self.end_row == 7)
        self.castled: bool = self.piece_moved[1] == "K" and (abs(self.start_col - self.end_col) >= 2)
        self.hash_code: int = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    def __eq__(self, other: Any) -> bool:
        """
        Takes in another object. Checks if other is another Move and if that move represents the same move.

        :param other: Another object
        :type other: Any
        :return: Checks if self and other have the same hash code
        :rtype: bool
        """
        if isinstance(other, Move):
            return self.hash_code == other.hash_code
        return False

    def set_en_passent(self, color):
        change = -1 if color == "w" else +1
        self.en_passent = (True, (self.start_row + change, self.start_col))

    def set_captured_en_passent(self, change: int):
        self.captured_en_passent = (True, (self.start_row, self.start_col + change))

    def get_chess_notation(self) -> str:
        """
        Presents the move in a readable way

        :return: A string that represents the move made
        :rtype: str
        """
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r: int, c: int) -> str:
        """
        Takes in a position and returns that position according to chess convention on rows and columns.

        :param r: String representing a row on the board
        :type r: int
        :param c: String representing a column in the board
        :type c: int
        :return: Returns a string representing the position according to chess convention on rows and columns
        :rtype: str
        """
        return self.cols_to_files[c] + self.rows_to_ranks[r]


class GameState:
    """
    This class is responsible for storing all the information about the current state of the chess game.
    Also, responsible for determining the valid moves at the current state, and keep a move-log.

    :param self.board: Represents the position of all the pieces
    :type self.board: List[List[str]]
    :param self.white_to_move: Represents whose turn it is
    :type self.white_to_move: bool
    :param self.move_log: A list of all the made moves to enable undoes and game exports
    :type self.move_log: List[str]
    """

    class CastlingRights:
        """
        Keeps tracks of the current castling rights of the GameState

        :param self.wks: Represents if white is able to king-side castle
        :type self.wks: bool
        :param self.wqs: Represents if white is able to queen-side castle
        :type self.wqs: bool
        :param self.bks: Represents if black is able to king-side castle
        :type self.bks: bool
        :param self.bqs: Represents if black is able to queen-side castle
        :type self.bqs: bool
        """

        def __init__(self, wks: bool = True, wqs: bool = True, bks: bool = True, bqs: bool = True):
            self.wks = wks
            self.wqs = wqs
            self.bks = bks
            self.bqs = bqs

    def __init__(self, board=STARTING_BOARD):
        self.board = board
        self.move_functions = {"p": self.generate_pawn_moves, "R": self.generate_rook_moves,
                               "N": self.generate_knight_moves, "B": self.generate_bishop_moves,
                               "K": self.generate_king_moves, "Q": self.generate_queen_moves}
        self.white_to_move = True
        self.move_log: List[Move] = []
        self.white_king_location = (7, 4)
        self.black_king_location = (0, 4)
        self.castling_rights = self.CastlingRights(True, True, True, True)
        self.castling_log = [self.CastlingRights(self.castling_rights.wks,
                                                 self.castling_rights.wqs,
                                                 self.castling_rights.bks,
                                                 self.castling_rights.bqs)]
        self.checkmate = False

    def make_move(self, move: Move):
        """
        Takes in a move made.
        Changes the GameState to reflect that move and adds it to the move log.

        :param move: Represents the move made
        :type move: Move
        """
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.handle_castling_rights(move)
        if move.pawn_promotion:
            promoting_piece = "Q"
            self.promote_pawn(move.end_row, move.end_col, move.piece_moved[0], promoting_piece)
        captured_en_passent = self.move_log[-1].captured_en_passent
        if captured_en_passent[0]:
            self.board[captured_en_passent[1][0]][captured_en_passent[1][1]] = "--"
        if move.piece_moved[1] == "K":
            prefix = move.piece_moved[0]
            castled = move.castled
            if castled:
                if move.end_col == 6:
                    self.board[move.end_row][5] = f"{prefix}R"
                    self.board[move.end_row][7] = "--"
                else:
                    self.board[move.end_row][3] = f"{prefix}R"
                    self.board[move.end_row][0] = "--"
            if prefix == "w":
                self.white_king_location = (move.end_row, move.end_col)
            else:
                self.black_king_location = (move.end_row, move.end_col)

        self.white_to_move = not self.white_to_move

    def undo(self):
        """
        Reverses the latest move in the move log.
        """
        if not self.move_log:
            return
        move = self.move_log.pop()
        self.board[move.start_row][move.start_col] = move.piece_moved
        self.board[move.end_row][move.end_col] = move.piece_captured
        self.white_to_move = not self.white_to_move
        if move.piece_moved == "wK":
            if move.castled:
                if move.end_col == 6:
                    self.board[move.end_row][5] = "--"
                    self.board[move.end_row][7] = "wR"
                else:
                    self.board[move.end_row][3] = "--"
                    self.board[move.end_row][0] = "wR"
            self.white_king_location = (move.start_row, move.start_col)
            self.castling_rights = self.castling_log.pop() if not len(self.castling_log) == 0 else self.castling_rights
        elif move.piece_moved == "bK":
            if move.castled:
                if move.end_col == 6:
                    self.board[move.end_row][5] = "--"
                    self.board[move.end_row][7] = "bR"
                else:
                    self.board[move.end_row][3] = "--"
                    self.board[move.end_row][0] = "bR"
            self.black_king_location = (move.start_row, move.start_col)
            self.castling_rights = self.castling_log.pop() if not len(self.castling_log) == 0 else self.castling_rights
        elif move.piece_moved[1] == "R":
            self.castling_rights = self.castling_log.pop() if not len(self.castling_log) == 0 else self.castling_rights
        if move.captured_en_passent[0]:
            self.board[move.captured_en_passent[1][0]][move.captured_en_passent[1][1]] = \
                "bp" if move.piece_moved == "wp" else "wp"

    def _valid_moves(self) -> List[Move]:
        """
        Filters possible moves by removing checks and then returns the moves.

        :return: Returns list of all valid moves for player excluding castling
        :rtype: List[Move]
        """
        moves = self.possible_moves()
        # OBS - Check this? Why filter for all moves all the time
        for i in range(len(moves) - 1, -1, -1):
            self.filter_invalid_moves(i, moves)
        if not moves:
            is_checkmate = self.in_check()
            self.checkmate = is_checkmate
        return moves

    def valid_moves(self) -> List[Move]:
        """
        Filters possible moves by removing checks and then returns the moves.

        :return: Returns list of all valid moves for player including castling
        :rtype: List[Move]
        """
        moves = self._valid_moves()
        moves = self.generate_castling_moves(moves)
        return moves

    def filter_invalid_moves(self, i, possible_moves: List[Move]):
        """
        Makes a possible move, then checks if the king is attacked by any opposing piece.
        If it is attacked, then that is an invalid move and that move is filtered out.

        :param i: Index of the possible move to be checked
        :type i: int
        :param possible_moves: All the possible moves to check
        :type possible_moves: List[Move]
        """
        move = possible_moves[i]
        self.make_move(move)
        self.white_to_move = not self.white_to_move
        remove_move = self.in_check()
        if remove_move:
            possible_moves.pop(i)
        self.white_to_move = not self.white_to_move
        self.undo()

    def possible_moves(self) -> List[Move]:
        """
        Returns all possible moves without regard for checks.

        :return: All possible moves without regard for checks
        :rtype: List[Move]
        """
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                ref = self.board[r][c]
                color = ref[0]
                if (color == "w" and self.white_to_move) or (color == "b" and not self.white_to_move):
                    self.move_functions[ref[1]](r, c, moves)
        return moves

    def generate_pawn_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the pawn at the current position to moves

        :param r: The current column of the pawn
        :type r: int
        :param c: The current row of the pawn
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        change = -1 if self.white_to_move else +1
        start_row = 6 if self.white_to_move else 1
        if self.board[r + change][c] == "--":
            moves.append(Move((r, c), (r + change, c), self.board))
            if r == start_row and self.board[r + (change * 2)][c] == "--":
                move = Move((r, c), (r + (change * 2), c), self.board)
                move.set_en_passent("w" if self.white_to_move else "b")
                moves.append(move)
        self.generate_attacking_pawn_moves(r, c, moves)

    def generate_attacking_pawn_moves(self, r: int, c: int, moves):
        """
        Appends all moves where a pawn attacks diagonally to moves

        :param r: The current column of the pawn
        :type r: int
        :param c: The current row of the pawn
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        prefix = "b" if self.white_to_move else "w"
        change = r - 1 if self.white_to_move else r + 1
        if change > 7 or change < 0:
            return
        if c - 1 >= 0 and self.board[change][c - 1][0] == prefix:
            moves.append(Move((r, c), (change, c - 1), self.board))
        if c + 1 <= 7 and self.board[change][c + 1][0] == prefix:
            moves.append(Move((r, c), (change, c + 1), self.board))
        en_passent = self.move_log[-1].en_passent if self.move_log else (False, (0, 0), (0, 0))
        if en_passent[0]:
            if en_passent[1] == (change, c + 1):
                move = Move((r, c), (change, c + 1), self.board)
                move.set_captured_en_passent(1)
                moves.append(move)
            elif en_passent[1] == (change, c - 1):
                move = Move((r, c), (change, c - 1), self.board)
                move.set_captured_en_passent(-1)
                moves.append(move)

    def generate_knight_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the knight at the current position to moves

        :param r: The current column of the knight
        :type r: int
        :param c: The current row of the knight
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        same_color = "w" if self.white_to_move else "b"
        deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
        potential_moves = map(lambda delta: (r + delta[0], c + delta[1]), deltas)
        results = filter(lambda move: self.valid_piece_position(move, same_color), potential_moves)
        for next_move in results:
            moves.append(Move((r, c), next_move, self.board))

    def generate_bishop_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the bishop at the current position to moves

        :param r: The current column of the bishop
        :type r: int
        :param c: The current row of the bishop
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]
        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while self.valid_piece_position(next_move, same_color) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])

    def generate_rook_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the rook at the current position to moves

        :param r: The current column of the rook
        :type r: int
        :param c: The current row of the rook
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, 0), (0, +1), (-1, 0), (0, -1)]

        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while self.valid_piece_position(next_move, same_color) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])

    def generate_queen_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the queen at the current position to moves

        :param r: The current column of the queen
        :type r: int
        :param c: The current row of the queen
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        same_color = "w" if self.white_to_move else "b"
        other_color = "b" if self.white_to_move else "w"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1), (+1, 0), (0, +1), (-1, 0), (0, -1)]
        for delta in deltas:
            next_move = (r + delta[0], c + delta[1])
            captures = False
            while self.valid_piece_position(next_move, same_color) and not captures:
                captures = self.board[next_move[0]][next_move[1]][0] == other_color
                moves.append(Move((r, c), next_move, self.board))
                next_move = (next_move[0] + delta[0], next_move[1] + delta[1])

    def generate_king_moves(self, r: int, c: int, moves: List[Move]):
        """
        Appends all possible legal moves made by the king at the current position to moves

        :param r: The current column of the king
        :type r: int
        :param c: The current row of the king
        :type c: int
        :param moves: All current valid moves
        :type moves: List[Move]
        """
        same_color = "w" if self.white_to_move else "b"
        deltas = [(+1, +1), (+1, -1), (-1, +1), (-1, -1), (+1, 0), (0, +1), (-1, 0), (0, -1)]
        potential_moves = map(lambda delta: (r + delta[0], c + delta[1]), deltas)
        results = filter(lambda move: self.valid_piece_position(move, same_color), potential_moves)
        for next_move in results:
            moves.append(Move((r, c), next_move, self.board))

    def generate_castling_moves(self, moves: List[Move]):
        """
        Generates the castling moves

        :param moves: current valid moves
        :type: List[Move]
        :return: all valid moves including castling
        :rtype: List[Move]
        """

        if self.white_to_move:
            ks, qs = self.castling_rights.wks, self.castling_rights.wqs
            last_row = self.board[7]
            if not last_row[5] == "--" or not last_row[6] == "--":
                ks = False
            if not last_row[3] == "--" or not last_row[2] == "--" or not last_row[1] == "--":
                qs = False
            if not (ks or qs):
                return moves
            wqB, wQ, wK, wkB, wN = self.square_is_attacked((7, 2)), \
                self.square_is_attacked((7, 3)), \
                self.square_is_attacked((7, 4)), \
                self.square_is_attacked((7, 5)), \
                self.square_is_attacked((7, 6))
            if wkB or wN or wK:
                ks = False
            if wqB or wQ or wK:
                qs = False
            if ks:
                moves.append(Move((7, 4), (7, 6), self.board))
            if qs:
                moves.append(Move((7, 4), (7, 2), self.board))
        else:
            ks, qs = self.castling_rights.bks, self.castling_rights.bqs
            last_row = self.board[0]
            if not last_row[5] == "--" or not last_row[6] == "--":
                ks = False
            if not last_row[3] == "--" or not last_row[2] == "--" or not last_row[1] == "--":
                qs = False
            if not (ks or qs):
                return moves
            bqB, bQ, bK, bkB, bN = self.square_is_attacked((0, 2)), \
                self.square_is_attacked((0, 3)), \
                self.square_is_attacked((0, 4)), \
                self.square_is_attacked((0, 5)), \
                self.square_is_attacked((0, 6))
            if bkB or bN or bK:
                ks = False
            if bqB or bQ or bK:
                qs = False
            if ks:
                moves.append(Move((0, 4), (0, 6), self.board))
            if qs:
                moves.append(Move((0, 4), (0, 2), self.board))
        return moves

    def valid_piece_position(self, move: Tuple[int, int], same_color: str) -> bool:
        """
        Takes in a tuple representing the ending squares and a string of the color of the moving piece.
        Returns True if the move is within bounds and not landing on another piece of the same color.

        :param move: A tuple representing the ending moves row and column
        :type move: Tuple[int, int]
        :param same_color: A string representing the color of the moving piece, either w or b
        :type same_color: str
        :return: A boolean declaring if the move is within bounds and not ending on a piece of the same color
        :rtype: bool
        """
        return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and self.board[move[0]][move[1]][0] != same_color

    def square_is_attacked(self, square: Tuple[int, int]) -> bool:
        """
        Returns True if the square is attacked by one of the other colors pieces,
        otherwise False.

        :param square: The square we check if it is attacked
        :type: Tuple[int, int]
        :return: True if the square is attacked, otherwise false
        :rtype: bool
        """
        prefix = "b" if self.white_to_move else "w"
        moves: List[Move] = []
        self.generate_attacking_pawn_moves(square[0], square[1], moves)
        for pawn_move in moves:
            if self.board[pawn_move.end_row][pawn_move.end_col] == f"{prefix}p":
                return True
        moves: List[Move] = []
        self.generate_bishop_moves(square[0], square[1], moves)
        for bishop_move in moves:
            if self.board[bishop_move.end_row][bishop_move.end_col] == f"{prefix}B":
                return True
        moves: List[Move] = []
        self.generate_knight_moves(square[0], square[1], moves)
        for knight_move in moves:
            if self.board[knight_move.end_row][knight_move.end_col] == f"{prefix}N":
                return True
        moves: List[Move] = []
        self.generate_rook_moves(square[0], square[1], moves)
        for rook_move in moves:
            if self.board[rook_move.end_row][rook_move.end_col] == f"{prefix}R":
                return True
        moves: List[Move] = []
        self.generate_queen_moves(square[0], square[1], moves)
        for queen_move in moves:
            if self.board[queen_move.end_row][queen_move.end_col] == f"{prefix}Q":
                return True
        moves: List[Move] = []
        self.generate_king_moves(square[0], square[1], moves)
        for king_move in moves:
            if self.board[king_move.end_row][king_move.end_col] == f"{prefix}K":
                return True
        return False

    def in_check(self) -> bool:
        """
        Returns true if king is in check, otherwise returns false.

        :return: If the king is in check
        :rtype: bool
        """
        position = self.white_king_location if self.white_to_move else self.black_king_location
        return self.square_is_attacked(position)

    def promote_pawn(self, r: int, c: int, color: str, new_piece: str):
        self.board[r][c] = color + new_piece

    def handle_castling_rights(self, move: Move):
        """
        Takes in a move and potentially updates the castling rights

        :param move: The move that can remove castling rights
        """
        if move.piece_moved == "wK":
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(False, False, rights.bks, rights.bqs)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
        if move.piece_moved == "bK":
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(rights.wks, rights.wqs, False, False)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
        if move.piece_moved == "wR" and move.start_col == 7:
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(False, rights.wqs, rights.bks, rights.bqs)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
        if move.piece_moved == "wR" and move.start_col == 0:
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(rights.wks, False, rights.bks, rights.bqs)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
        if move.piece_moved == "bR" and move.start_col == 7:
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(rights.wks, rights.wqs, False, rights.bqs)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
        if move.piece_moved == "bR" and move.start_col == 0:
            rights = self.castling_rights
            self.castling_rights = self.CastlingRights(rights.wks, rights.wqs, rights.bks, False)
            self.castling_log.append(self.CastlingRights(rights.wks, rights.wqs, rights.bks, rights.bqs))
