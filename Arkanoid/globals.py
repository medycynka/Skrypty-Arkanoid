import pygame


# SCREEN properties
WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
TITLE = "Basic Arkanoid by Szymon Peszek"

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PALEBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
LIGHT_GREY = (220, 220, 220)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

# Event types
CLOSE_WINDOW = pygame.QUIT
KEYDOWN_EVENT = pygame.KEYDOWN
ESC_KEY = pygame.K_ESCAPE
Q_KEY = pygame.K_q
LEFT_A = pygame.K_LEFT
RIGHT_A = pygame.K_RIGHT
P_KEY = pygame.K_p
R_KEY = pygame.K_r
CLICK = pygame.MOUSEBUTTONDOWN

# Game Properties
SPRITES = pygame.sprite.Group()
BRICKS = pygame.sprite.Group()
MOVE_AMOUNT = 5
BRICK_WIDTH = 100
BRICK_HEIGHT = 30
SPACING = 3
