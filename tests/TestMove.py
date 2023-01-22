import unittest

from src.ChessEngine import Move


class MyTestCase(unittest.TestCase):
    def test_pawn_promotion(self):
        board_one = [
            ["--", "--", "bQ", "--", "--", "--", "--", "--"],
            ["--", "wp", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        move_one = Move((1, 1), (0, 2), board_one)

        board_two = [
            ["--", "--", "--", "--", "bK", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "wK", "--"],
            ["--", "--", "bp", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        move_two = Move((6, 2), (7, 2), board_two)

        board_three = [
            ["--", "--", "bQ", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "wp", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        move_three = Move((2, 1), (1, 0), board_three)

        board_four = [
            ["--", "--", "bQ", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "wp"],
            ["--", "wp", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        move_four = Move((0, 7), (0, 6), board_four)

        self.assertTrue(move_one.pawn_promotion,
                        "Pawn moved to row 8, therefore the move should be a promotion")
        self.assertTrue(move_two.pawn_promotion,
                        "Pawn moved to row 0, therefore the move should be a promotion")

        self.assertFalse(move_three.pawn_promotion,
                         "Pawn moved to row 7, therefore the move should not be a promotion")
        self.assertFalse(move_four.pawn_promotion,
                         "The piece being moved isn't a pawn, therefore it shouldn't be a promotion")

    def test_en_passent(self):
        board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        move = Move((6, 0), (4, 0), board)
        move.set_en_passent("w")

        self.assertEqual((True, (5, 0)), move.en_passent,
                         "Pawn moved two squares in one turn so should be able to be captured en passent")

    def test_captured_en_passent(self):
        board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "--", "--", "bp", "bp", "bp"],
            ["--", "--", "--", "wp", "bp", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        move = Move((3, 4), (2, 3), board)
        move.set_captured_en_passent("w")

        self.assertEqual((True, (3, 3)), move.captured_en_passent,
                         "Pawn captured en passent, flag should indicate captured pawns position")


if __name__ == '__main__':
    unittest.main()
