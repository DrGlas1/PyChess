import unittest

from src.ChessEngine import Move, GameState


class MyTestCase(unittest.TestCase):
    def test_all_possible_moves(self):
        board_one = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        correct_moves_one = [
            Move((6, 0), (5, 0), board_one), Move((6, 0), (4, 0), board_one),
            Move((6, 1), (5, 1), board_one), Move((6, 1), (4, 1), board_one),
            Move((6, 2), (5, 2), board_one), Move((6, 2), (4, 2), board_one),
            Move((6, 3), (5, 3), board_one), Move((6, 3), (4, 3), board_one),
            Move((6, 4), (5, 4), board_one), Move((6, 4), (4, 4), board_one),
            Move((6, 5), (5, 5), board_one), Move((6, 5), (4, 5), board_one),
            Move((6, 6), (5, 6), board_one), Move((6, 6), (4, 6), board_one),
            Move((6, 7), (5, 7), board_one), Move((6, 7), (4, 7), board_one),
            Move((7, 1), (5, 0), board_one), Move((7, 1), (5, 2), board_one),
            Move((7, 6), (5, 5), board_one), Move((7, 6), (5, 7), board_one),
        ]
        gs_one = GameState(board_one)
        test_moves_one = gs_one.possible_moves()

        board_two = [
            ["bR", "--", "bB", "bQ", "bK", "bB", "--", "bR"],
            ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
            ["--", "--", "bN", "--", "--", "bN", "--", "--"],
            ["--", "wB", "--", "--", "bp", "--", "--", "--"],
            ["--", "--", "--", "--", "wp", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "--", "--", "wR"]
        ]

        correct_moves_two = [
            Move((3, 1), (4, 2), board_two), Move((3, 1), (5, 3), board_two),
            Move((3, 1), (6, 4), board_two), Move((3, 1), (7, 5), board_two),
            Move((3, 1), (4, 0), board_two), Move((3, 1), (2, 2), board_two),
            Move((3, 1), (2, 0), board_two), Move((6, 0), (5, 0), board_two),
            Move((6, 0), (4, 0), board_two), Move((6, 1), (5, 1), board_two),
            Move((6, 1), (4, 1), board_two), Move((6, 2), (5, 2), board_two),
            Move((6, 2), (4, 2), board_two), Move((6, 3), (5, 3), board_two),
            Move((6, 3), (4, 3), board_two), Move((6, 5), (5, 5), board_two),
            Move((6, 5), (4, 5), board_two), Move((6, 6), (5, 6), board_two),
            Move((6, 6), (4, 6), board_two), Move((6, 7), (5, 7), board_two),
            Move((6, 7), (4, 7), board_two), Move((7, 1), (5, 0), board_two),
            Move((7, 1), (5, 2), board_two), Move((7, 3), (6, 4), board_two),
            Move((7, 3), (5, 5), board_two), Move((7, 3), (4, 6), board_two),
            Move((7, 3), (3, 7), board_two), Move((7, 4), (7, 5), board_two),
            Move((7, 4), (6, 4), board_two), Move((7, 7), (7, 6), board_two),
            Move((7, 7), (7, 5), board_two)
        ]
        gs_two = GameState(board_two)
        test_moves_two = gs_two.possible_moves()

        board_three = [
            ["--", "--", "--", "--", "--", "--", "--", "bK"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wp"],
            ["--", "--", "--", "--", "--", "wQ", "wK", "--"],
            ["--", "--", "--", "--", "--", "--", "bp", "--"],
            ["--", "--", "--", "--", "bQ", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        correct_moves_three = [
            Move((2, 7), (1, 7), board_three), Move((3, 5), (4, 6), board_three),
            Move((3, 5), (4, 4), board_three), Move((3, 5), (5, 3), board_three),
            Move((3, 5), (6, 2), board_three), Move((3, 5), (7, 1), board_three),
            Move((3, 5), (2, 6), board_three), Move((3, 5), (1, 7), board_three),
            Move((3, 5), (2, 4), board_three), Move((3, 5), (1, 3), board_three),
            Move((3, 5), (0, 2), board_three), Move((3, 5), (4, 5), board_three),
            Move((3, 5), (5, 5), board_three), Move((3, 5), (6, 5), board_three),
            Move((3, 5), (7, 5), board_three), Move((3, 5), (2, 5), board_three),
            Move((3, 5), (1, 5), board_three), Move((3, 5), (0, 5), board_three),
            Move((3, 5), (3, 4), board_three), Move((3, 5), (3, 3), board_three),
            Move((3, 5), (3, 2), board_three), Move((3, 5), (3, 1), board_three),
            Move((3, 5), (3, 0), board_three), Move((3, 6), (4, 7), board_three),
            Move((3, 6), (4, 5), board_three), Move((3, 6), (2, 5), board_three),
            Move((3, 6), (4, 6), board_three), Move((3, 6), (3, 7), board_three),
            Move((3, 6), (2, 6), board_three),
        ]
        gs_three = GameState(board_three)
        test_moves_three = gs_three.possible_moves()

        # Tests first board
        self.assertEqual(len(test_moves_one), len(correct_moves_one),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves_one)} but was {len(test_moves_one)}")
        for move in test_moves_one:
            self.assertTrue(move in correct_moves_one,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests second board
        self.assertEqual(len(test_moves_two), len(correct_moves_two),
                         f"Incorrect number of valid moves for second board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_two:
            self.assertTrue(move in correct_moves_two,
                            f"Incorrect move added for second board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests third board
        self.assertEqual(len(test_moves_three), len(correct_moves_three),
                         f"Incorrect number of valid moves for third board, should be "
                         f"{len(correct_moves_three)} but was {len(test_moves_three)}")
        for move in test_moves_three:
            self.assertTrue(move in correct_moves_three,
                            f"Incorrect move added for third board"
                            f", piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_pawn_attacking_moves(self):
        board_one = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', '--', '--', '--', 'wp'],
            ['--', '--', '--', '--', 'bp', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', '--', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

        gs_one = GameState(board_one)

        self.assertTrue(Move((1, 7), (0, 6), board_one) in gs_one.possible_moves(),
                        "Pawn on edge of board cannot attack")

    def test_pawn_checks(self):
        pawn_board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bp", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wK", "--", "--", "--"]
        ]

        correct_pawn = [
            Move((7, 4), (7, 5), pawn_board), Move((7, 4), (6, 4), pawn_board),
            Move((7, 4), (7, 3), pawn_board)
        ]

        gs = GameState(pawn_board)
        test_moves = gs.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves), len(correct_pawn),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_pawn)} but was {len(test_moves)}")
        for move in test_moves:
            self.assertTrue(move in correct_pawn,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_rook_checks(self):
        rook_board_one = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_one = [
            Move((7, 7), (7, 6), rook_board_one), Move((7, 7), (6, 6), rook_board_one),
        ]

        gs_one = GameState(rook_board_one)
        test_moves_one = gs_one.valid_moves()

        rook_board_two = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wQ"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_two = [
            Move((7, 7), (7, 6), rook_board_one), Move((7, 7), (6, 6), rook_board_one),
            Move((4, 7), (0, 7), rook_board_two), Move((4, 7), (1, 7), rook_board_two),
            Move((4, 7), (2, 7), rook_board_two), Move((4, 7), (3, 7), rook_board_two),
            Move((4, 7), (5, 7), rook_board_two), Move((4, 7), (6, 7), rook_board_two),
            Move((7, 7), (6, 7), rook_board_two)]

        gs_two = GameState(rook_board_two)
        test_moves_two = gs_two.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves_one), len(correct_moves_one),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_one)}")
        for move in test_moves_one:
            self.assertTrue(move in correct_moves_one,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests second board
        self.assertEqual(len(test_moves_two), len(correct_moves_two),
                         f"Incorrect number of valid moves for second board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_two:
            self.assertTrue(move in correct_moves_two,
                            f"Incorrect move added for second board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_bishop_checks(self):
        bishop_board_one = [
            ["bB", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_one = [
            Move((7, 7), (7, 6), bishop_board_one), Move((7, 7), (6, 7), bishop_board_one),
        ]

        gs_one = GameState(bishop_board_one)
        test_moves_one = gs_one.valid_moves()

        bishop_board_two = [
            ["bB", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wQ", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_two = [
            Move((7, 7), (7, 6), bishop_board_one), Move((7, 7), (6, 7), bishop_board_one),
            Move((7, 7), (6, 6), bishop_board_one), Move((4, 4), (3, 3), bishop_board_two),
            Move((4, 4), (2, 2), bishop_board_two), Move((4, 4), (1, 1), bishop_board_two),
            Move((4, 4), (5, 5), bishop_board_two), Move((4, 4), (6, 6), bishop_board_two),
            Move((4, 4), (0, 0), bishop_board_two)]

        gs_two = GameState(bishop_board_two)
        test_moves_two = gs_two.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves_one), len(correct_moves_one),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_one)}")
        for move in test_moves_one:
            self.assertTrue(move in correct_moves_one,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests second board
        self.assertEqual(len(test_moves_two), len(correct_moves_two),
                         f"Incorrect number of valid moves for second board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_two:
            self.assertTrue(move in correct_moves_two,
                            f"Incorrect move added for second board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_queen_checks(self):
        queen_board_one = [
            ["bQ", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_one = [
            Move((7, 7), (7, 6), queen_board_one), Move((7, 7), (6, 7), queen_board_one)
        ]

        gs_one = GameState(queen_board_one)
        test_moves_one = gs_one.valid_moves()

        queen_board_two = [
            ["bQ", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wQ", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_two = [
            Move((7, 7), (7, 6), queen_board_one), Move((7, 7), (6, 7), queen_board_one),
            Move((7, 7), (6, 6), queen_board_one), Move((4, 4), (3, 3), queen_board_two),
            Move((4, 4), (2, 2), queen_board_two), Move((4, 4), (1, 1), queen_board_two),
            Move((4, 4), (5, 5), queen_board_two), Move((4, 4), (6, 6), queen_board_two),
            Move((4, 4), (0, 0), queen_board_two)]

        gs_two = GameState(queen_board_two)
        test_moves_two = gs_two.valid_moves()

        queen_board_three = [
            ["--", "--", "--", "--", "--", "--", "--", "bQ"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_three = [
            Move((7, 7), (7, 6), queen_board_three), Move((7, 7), (6, 6), queen_board_three),
        ]

        gs_three = GameState(queen_board_three)
        test_moves_three = gs_three.valid_moves()

        queen_board_four = [
            ["--", "--", "--", "--", "--", "--", "--", "bQ"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wQ"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        correct_moves_four = [
            Move((7, 7), (7, 6), queen_board_three), Move((7, 7), (6, 6), queen_board_three),
            Move((4, 7), (0, 7), queen_board_four), Move((4, 7), (1, 7), queen_board_four),
            Move((4, 7), (2, 7), queen_board_four), Move((4, 7), (3, 7), queen_board_four),
            Move((4, 7), (5, 7), queen_board_four), Move((4, 7), (6, 7), queen_board_four),
            Move((7, 7), (6, 7), queen_board_four)]

        gs_four = GameState(queen_board_four)
        test_moves_four = gs_four.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves_one), len(correct_moves_one),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves_one)} but was {len(test_moves_one)}")
        for move in test_moves_one:
            self.assertTrue(move in correct_moves_one,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests second board
        self.assertEqual(len(test_moves_two), len(correct_moves_two),
                         f"Incorrect number of valid moves for second board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_two:
            self.assertTrue(move in correct_moves_two,
                            f"Incorrect move added for second board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests third board
        self.assertEqual(len(test_moves_three), len(correct_moves_three),
                         f"Incorrect number of valid moves for third board, should be "
                         f"{len(correct_moves_three)} but was {len(test_moves_three)}")
        for move in test_moves_three:
            self.assertTrue(move in correct_moves_three,
                            f"Incorrect move added for third board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests fourth board
        self.assertEqual(len(test_moves_four), len(correct_moves_four),
                         f"Incorrect number of valid moves for fourth board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_four:
            self.assertTrue(move in correct_moves_four,
                            f"Incorrect move added for fourth board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_knight_checks(self):
        knight_board_one = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bN", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wK", "--", "--", "--"]
        ]

        correct_moves_one = [
            Move((7, 4), (7, 5), knight_board_one), Move((7, 4), (6, 4), knight_board_one),
            Move((7, 4), (7, 3), knight_board_one)
        ]

        gs_one = GameState(knight_board_one)
        test_moves_one = gs_one.valid_moves()

        knight_board_two = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bN", "--", "wK", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        correct_moves_two = [
            Move((4, 6), (3, 5), knight_board_one), Move((4, 6), (4, 5), knight_board_one),
            Move((4, 6), (5, 5), knight_board_one), Move((4, 6), (3, 7), knight_board_one),
            Move((4, 6), (4, 7), knight_board_one), Move((4, 6), (5, 7), knight_board_one)
        ]

        gs_two = GameState(knight_board_two)
        test_moves_two = gs_two.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves_one), len(correct_moves_one),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves_one)} but was {len(test_moves_one)}")
        for move in test_moves_one:
            self.assertTrue(move in correct_moves_one,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

        # Tests second board
        self.assertEqual(len(test_moves_two), len(correct_moves_two),
                         f"Incorrect number of valid moves for second board, should be "
                         f"{len(correct_moves_two)} but was {len(test_moves_two)}")
        for move in test_moves_two:
            self.assertTrue(move in correct_moves_two,
                            f"Incorrect move added for second board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_king_checks(self):
        king_board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bK", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wK", "--", "--", "--"]
        ]

        correct_moves = [
            Move((7, 4), (7, 5), king_board), Move((7, 4), (7, 3), king_board)
        ]

        gs = GameState(king_board)
        test_moves = gs.valid_moves()

        # Tests first board
        self.assertEqual(len(test_moves), len(correct_moves),
                         f"Incorrect number of valid moves for first board, should be "
                         f"{len(correct_moves)} but was {len(test_moves)}")
        for move in test_moves:
            self.assertTrue(move in correct_moves,
                            f"Incorrect move added for first board, "
                            f"piece {move.piece_moved} moved {move.get_chess_notation()}")

    def test_in_check(self):
        pawn_board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bp", "--", "--", "--"],
            ["--", "--", "--", "wK", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        pawn_gs = GameState(pawn_board)
        pawn_gs.white_king_location = (6, 3)

        rook_board = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        rook_gs = GameState(rook_board)
        rook_gs.white_king_location = (7, 7)

        bishop_board = [
            ["bB", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        bishop_gs = GameState(bishop_board)
        bishop_gs.white_king_location = (7, 7)

        queen_board = [
            ["bQ", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        queen_gs = GameState(queen_board)
        queen_gs.white_king_location = (7, 7)

        knight_board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bN", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wK", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        knight_gs = GameState(knight_board)
        knight_gs.white_king_location = (6, 3)

        no_check_board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        no_check_gs = GameState(no_check_board)

        self.assertTrue(pawn_gs.in_check(), "King should be in check from pawn")
        self.assertTrue(knight_gs.in_check(), "King should be in check from knight")
        self.assertTrue(bishop_gs.in_check(), "King should be in check from bishop")
        self.assertTrue(rook_gs.in_check(), "King should be in check from rook")
        self.assertTrue(queen_gs.in_check(), "King should be in check from queen")
        self.assertFalse(no_check_gs.in_check(), "King should not be in check from any piece")

    def test_checkmate(self):
        queen_checkmate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bK", "--"],
            ["--", "--", "--", "--", "--", "--", "bQ", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        bishop_checkmate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bK", "--"],
            ["--", "--", "--", "--", "--", "bB", "bB", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        knight_checkmate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "bN", "bK", "--"],
            ["--", "--", "--", "--", "--", "bN", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        rook_checkmate = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "bK", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        no_checkmate_one_board = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bk", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        no_checkmate_two_board = [
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bQ", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        checkmate_one = GameState(queen_checkmate)
        checkmate_two = GameState(bishop_checkmate)
        checkmate_three = GameState(knight_checkmate)
        checkmate_four = GameState(rook_checkmate)

        no_checkmate_one = GameState(no_checkmate_one_board)
        no_checkmate_two = GameState(no_checkmate_two_board)

        checkmate_one.white_king_location = (7, 7)
        checkmate_two.white_king_location = (7, 7)
        checkmate_three.white_king_location = (7, 7)
        checkmate_four.white_king_location = (7, 7)

        no_checkmate_one.white_king_location = (7, 7)
        no_checkmate_two.white_king_location = (7, 7)

        self.assertTrue(checkmate_one.in_check() and not checkmate_one.valid_moves(),
                        "King should be in checkmate from queen")
        self.assertTrue(checkmate_two.in_check() and not checkmate_two.valid_moves(),
                        "King should be in checkmate from bishops")
        self.assertTrue(checkmate_three.in_check() and not checkmate_three.valid_moves(),
                        "King should be in checkmate from knights")
        self.assertTrue(checkmate_four.in_check() and not checkmate_four.valid_moves(),
                        "King should be in checkmate from rook")

        self.assertFalse(no_checkmate_one.in_check() and not no_checkmate_one.valid_moves(),
                         "King should not be in checkmate because Kg1 is a legal move")
        self.assertFalse(no_checkmate_two.in_check() and not no_checkmate_two.valid_moves(),
                         "King should not be in checkmate because Kxg2 is a legal move")

    def test_stalemate(self):
        queen_stalemate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bK", "--"],
            ["--", "--", "--", "--", "--", "--", "bQ", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        rook_stalemate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "bK", "bR", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        no_stalemate = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "bK", "bQ"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wK"]
        ]

        stalemate_one = GameState(queen_stalemate)
        stalemate_two = GameState(rook_stalemate)

        no_stalemate = GameState(no_stalemate)

        stalemate_one.white_king_location = (7, 7)
        stalemate_two.white_king_location = (7, 7)

        no_stalemate.white_king_location = (7, 7)

        self.assertTrue(not stalemate_one.in_check() and not stalemate_one.valid_moves(),
                        "Should be stalemate as there are no legal moves")
        self.assertTrue(not stalemate_two.in_check() and not stalemate_two.valid_moves(),
                        "Should be stalemate as there are no legal moves")

        self.assertFalse(not no_stalemate.in_check() and not no_stalemate.valid_moves(),
                         "Should not be stalemate as Kg1 is a legal move")

    def test_undo(self):
        first_board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "bN", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wK", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        first_gs = GameState(first_board)
        first_gs.make_test_move(Move((6, 3), (7, 3), first_board))
        first_gs.undo()

        second_board = [
            ["--", "--", "bQ", "--", "--", "--", "--", "--"],
            ["--", "wp", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        second_gs = GameState(second_board)
        second_gs.make_test_move(Move((1, 1), (0, 2), second_board))
        second_gs.undo()

        self.assertEqual(first_gs.board, first_board,
                         "Undo does not return the board to the correct game state")
        self.assertEqual(second_gs.board, second_board,
                         "Undo does not return the board to the correct game state")

    def test_pawn_promotion(self):
        board_one = [
            ["--", "--", "wp", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        gs_one = GameState(board_one)
        gs_one.promote_pawn(0, 2, "w", "Q")

        self.assertEqual(gs_one.board[0][2], "wQ",
                         "Promotion didn't change the pawn to a white queen")

    def test_en_passent(self):
        board_one = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        board_one_first_check = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "--", "bp", "--", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "bp", "wp", "bp", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        board_one_second_check = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "--", "bp", "--", "bp", "bp"],
            ["--", "--", "--", "wp", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "bp", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        gs = GameState(board_one)
        move_one_w = Move((6, 4), (4, 4), gs.board)
        gs.make_move(move_one_w)
        move_one_b = Move((1, 5), (3, 5), gs.board)
        move_one_b.set_en_passent("b")
        gs.make_move(move_one_b)
        move_two_w = Move((4, 4), (3, 4), gs.board)
        gs.make_move(move_two_w)
        move_two_b = Move((1, 3), (3, 3), gs.board)
        move_two_b.set_en_passent("b")
        gs.make_move(move_two_b)

        self.assertEqual(gs.board, board_one_first_check, "Moves are not correctly changing the board")

        valid_moves = gs.valid_moves()
        move_three_w = Move((3, 4), (2, 3), gs.board)
        move_three_w.set_captured_en_passent(-1)
        fake_move_three_w = Move((3, 4), (2, 5), gs.board)

        self.assertTrue(move_three_w in valid_moves, "En passent should be possible because black d-pawn made a "
                                                     "double move last move")
        self.assertFalse(fake_move_three_w in valid_moves, "En passent should not be possible because black f-pawn"
                                                           "didn't make a double move last move")

        gs.make_move(move_three_w)
        self.assertEqual(gs.board, board_one_second_check, "After a captured en passent, the board is not correct")

        gs.undo()
        self.assertEqual(gs.board, board_one_first_check, "Undo of en passent does not return right board")

    def test_handle_castling_rights(self):
        board_one = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        gs = GameState(board_one)

        rights = gs.castling_rights
        self.assertTrue(rights.wks and rights.wqs and rights.bks and rights.bqs,
                        "At start of game, both sides should have their castling rights")

        move_one_w = Move((6, 4), (4, 4), gs.board)
        move_one_b = Move((1, 4), (3, 4), gs.board)
        move_two_w = Move((7, 4), (6, 4), gs.board)
        move_two_b = Move((0, 4), (1, 4), gs.board)
        gs.make_move(move_one_w)
        gs.make_move(move_one_b)
        gs.make_move(move_two_w)

        self.assertTrue(not rights.wks and not rights.wqs and rights.bks and rights.bqs,
                        "White should lose castling privileges after moving his king")

        gs.make_move(move_two_b)

        self.assertTrue(not rights.wks and not rights.wqs and not rights.bks and not rights.bqs,
                        "If both players have moved their kings and neither "
                        "should therefore have castling rights")
        gs.undo()
        gs.undo()

        self.assertTrue(rights.wks and rights.wqs and rights.bks and rights.bqs,
                        "Undoing should give back castling rights")

    def test_can_x_castle(self):
        board_one = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        board_one_first_check = [
            ["bR", "--", "bB", "bQ", "bK", "bB", "--", "bR"],
            ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
            ["--", "--", "bN", "--", "--", "bN", "--", "--"],
            ["--", "wB", "--", "--", "bp", "--", "--", "--"],
            ["--", "--", "--", "--", "wp", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "wN", "--", "--"],
            ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "--", "--", "wR"]
        ]

        gs = GameState(board_one)

        self.assertFalse(gs.can_white_short_castle(),
                         "No castling should be allowed on first move")
        self.assertFalse(gs.can_white_short_castle(),
                         "No castling should be allowed on first move")
        self.assertFalse(gs.can_black_short_castle(),
                         "No castling should be allowed on first move")
        self.assertFalse(gs.can_black_long_castle(),
                         "No castling should be allowed on first move")

        move_one_w = Move((6, 4), (4, 4), gs.board)
        move_one_b = Move((1, 4), (3, 4), gs.board)
        move_two_w = Move((7, 6), (5, 5), gs.board)
        move_two_b = Move((0, 1), (2, 2), gs.board)
        move_three_w = Move((7, 5), (3, 1), gs.board)
        move_three_b = Move((0, 6), (2, 5), gs.board)
        gs.make_move(move_one_w)
        gs.make_move(move_one_b)
        gs.make_move(move_two_w)
        gs.make_move(move_two_b)
        gs.make_move(move_three_w)
        gs.make_move(move_three_b)

        self.assertEqual(gs.board, board_one_first_check,
                         "Incorrect board, should not have passed previous tests")
        self.assertTrue(gs.can_white_short_castle(), "No pieces between king and kingsrook, "
                                                     "white should be able to castle")
        self.assertFalse(gs.can_white_long_castle() or
                         gs.can_black_short_castle() or gs.can_black_long_castle(),
                         "Castling allowed should be white's kingside castling")


if __name__ == '__main__':
    unittest.main()
