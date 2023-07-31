"""
The main file responsible for handling user input and displaying the current GameState object
"""

import pygame as p
from typing import List
from ChessEngine import GameState
from ChessEngine import Move

p.init()

WIDTH = HEIGHT = 512                    # Window size
DIMENSION = 8                           # Chessboard size
SQUARE_SIZE = WIDTH // DIMENSION        # Square size
MAX_FPS = 15                            # Highest number of frames per second for animation
IMAGES = {}                             # Images for displaying the chess pieces
LIGHT_SQUARE_COLOR = "White"            # The color of the light squares
DARK_SQUARE_COLOR = "Grey"              # The color of the dark squares


def load_images():
    """
    Initialize a global dictionary of images. This will be called only once in the main
    """
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    """
    The main driver for our code.
    Handle user input and updating the graphics in the game loop
    """
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = GameState()
    load_images()
    running = True
    sq_selected = ()                                   # Tuple with the square that the player last selected
    player_clicks = []                                 # Array of the last two selected squares
    valid_moves = gs.valid_moves()
    move_made = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undo()
                    move_made = True
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                c = location[0] // SQUARE_SIZE
                r = location[1] // SQUARE_SIZE
                if sq_selected == (r, c):              # Clicking on the same piece deselects the clicks
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (r, c)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2:
                    move = Move(player_clicks[0], player_clicks[1], gs.board)
                    for i in range(len(valid_moves)):
                        if move == valid_moves[i]:
                            gs.make_move(valid_moves[i])
                            move_made = True
                            sq_selected = ()
                            player_clicks = []
                            break
                    if not move_made:
                        player_clicks = [sq_selected]
        if move_made:
            valid_moves = gs.valid_moves()
            if not valid_moves:
                running = False
                is_checkmate = gs.checkmate
                print("Checkmate!") if is_checkmate else print("Stalemate :/")
            move_made = False
        clock.tick(MAX_FPS)
        p.display.flip()
        draw_game_state(screen, gs)


def draw_game_state(screen: p.Surface, gs: GameState):
    """
    Takes in a screen representing the board and the current GameState
    Draws the board and the pieces

    :param screen: Shows the current user interface
    :type screen: p.Surface
    :param gs: Holds information about the current board state
    :type gs: GameState
    """
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen: p.Surface):
    """
    Takes in a screen representing the board.
    Draws the board

    :param screen: Shows the current user interface
    :type screen: p.Surface
    """
    colors = [p.Color(LIGHT_SQUARE_COLOR), p.Color(DARK_SQUARE_COLOR)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # Light squares have even parity and dark squares have odd parity on a chess board
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen: p.Surface, board: List[List[str]]):
    """
    Takes in a screen representing the board and the current board.
    Draws the pieces on the board

    :param screen: Shows the current user interface
    :type screen: p.Surface
    :param board: Shows the current position of the pieces
    :type board: List[List{str]]
    """
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()
