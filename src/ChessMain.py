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
LIGHT_SQUARE_COLOR = "White"            # The color of the light squares
DARK_SQUARE_COLOR = "Grey"              # The color of the dark squares


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
    sq_selected = ()                                   # Tuple with the square that the player last selected
    player_clicks = []                                 # Array of the last two selected squares
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()           # (x, y) location of the mouse
                c = location[0] // SQUARE_SIZE
                r = location[1] // SQUARE_SIZE
                if sq_selected == (r, c):              # Clicking on the same piece deselects the clicks
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (r, c)
                    player_clicks.append(sq_selected)
                    print(sq_selected)
                    print(player_clicks)
                if len(player_clicks) == 2:
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    sq_selected = ()
                    player_clicks = []
        clock.tick(MAX_FPS)
        p.display.flip()
        draw_game_state(screen, gs)


def draw_game_state(screen, gs):
    """Draws the squares and the pieces on the board"""
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    """Draws the squares of the board"""
    colors = [p.Color(LIGHT_SQUARE_COLOR), p.Color(DARK_SQUARE_COLOR)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # Light squares have even parity and dark squares have odd parity on a chess board
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board):
    """Draws the pieces onto the current GameState.board"""
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()
