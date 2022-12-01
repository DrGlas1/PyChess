"""
The main file responsible for handling user input and displaying the current GameState object
"""

import pygame as p
from src import ChessEngine

p.init()

WIDTH = HEIGHT = 512                    # Window size
DIMENSION = 8                           # Chessboard size
SQUARE_SIZE = WIDTH // DIMENSION        # Square size
MAX_FPS = 15                            # Highest number of frames per second for animation
IMAGES = {}                             # Images for displaying the chess pieces


def load_images():
    """Initialize a global dictionary of images. This will be called only once in the main"""
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    """The main driver for our code. This will handle user input and updating the graphics"""
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(MAX_FPS)
        p.display.flip()
        draw_game_state(screen,gs)


def draw_game_state(screen, gs):
    """Draws the squares and the pieces on the board"""
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = [p.Color("White"), p.Color("Grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # Light squares have even parity and dark squares have odd parity on a chess board
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board):
    pass


if __name__ == "__main__":
    main()
