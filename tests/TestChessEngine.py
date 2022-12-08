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


if __name__ == '__main__':
    unittest.main()
