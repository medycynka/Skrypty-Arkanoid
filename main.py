import pygame
import player
import ball
import brick
from typing import List


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

# Game Properties
PLAY = True
PAUSE = False
SCORE = 0
LIVES = 1
SPRITES = pygame.sprite.Group()
BRICKS = pygame.sprite.Group()
MOVE_AMOUNT = 5
BRICK_WIDTH = 100
BRICK_HEIGHT = 30
SPACING = 3
LEVELS = 3
LVL1_COMPLETE = False
LVL2_COMPLETE = False
LVL3_COMPLETE = False


def set_up(start_x: int, start_y: int, col: int, colors: List) -> (player.Player, ball.Ball, pygame.font.Font):
    pygame.init()
    pygame.display.set_caption(TITLE)
    f = pygame.font.Font(None, 34)

    p = player.Player(WIDTH, HEIGHT, 100, 10, LIGHTBLUE, BLACK)
    p.rect.x = int((WIDTH - 100) / 2)
    p.rect.y = HEIGHT - 40

    bo = ball.Ball(10, 10, 4, BLACK, WHITE)
    bo.rect.x = 345
    bo.rect.y = 195

    generate_bricks(start_x, start_y, col, colors)

    SPRITES.add(p)
    SPRITES.add(bo)

    return p, bo, f


def generate_bricks(start_x: int, start_y: int, col: int, colors: List):
    if col != len(colors):
        raise ValueError("Number of columns and length of color's list must be the same!")

    line_count = int((WIDTH - (2 * 5 - SPACING)) / (BRICK_WIDTH + SPACING))
    for j in range(col):
        for i in range(line_count):
            br = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, BLACK, colors[j])
            br.rect.x = start_x + i * (BRICK_WIDTH + SPACING)
            br.rect.y = start_y + j * (BRICK_HEIGHT + SPACING)
            SPRITES.add(br)
            BRICKS.add(br)


if __name__ == '__main__':
    paddle, bouncer, FONT = set_up(35, 60, 3, [RED, ORANGE, YELLOW])

    while PLAY:
        # Event handling
        for event in pygame.event.get():
            if event.type == CLOSE_WINDOW:
                PLAY = False
            elif event.type == KEYDOWN_EVENT and (event.key == ESC_KEY or event.key == Q_KEY):
                PLAY = False
            elif event.type == KEYDOWN_EVENT and (event.key == P_KEY):
                PAUSE = True
                while PAUSE:
                    event = pygame.event.wait()

                    if event.type == KEYDOWN_EVENT and (event.key == P_KEY):
                        PAUSE = False
                    elif event.type == CLOSE_WINDOW:
                        PAUSE = False
                        PLAY = False
                    elif event.type == KEYDOWN_EVENT and (event.key == ESC_KEY or event.key == Q_KEY):
                        PAUSE = False
                        PLAY = False

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[LEFT_A]:
            paddle.move_left(MOVE_AMOUNT)
        if keys[RIGHT_A]:
            paddle.move_right(MOVE_AMOUNT)

        # Updating
        SPRITES.update()

        # Handle ball movement and collisions
        if bouncer.rect.x >= WIDTH - 10:
            bouncer.velocity[0] = -bouncer.velocity[0]
        if bouncer.rect.x <= 0:
            bouncer.velocity[0] = -bouncer.velocity[0]
        if bouncer.rect.y > HEIGHT - 10:
            bouncer.velocity[1] = -bouncer.velocity[1]
            LIVES -= 1

            if LIVES == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                SCREEN.blit(text, (int((WIDTH-300) / 2), 300))
                text = FONT.render("Press R to reset or esc/q to quit", 1, WHITE)
                SCREEN.blit(text, (int(WIDTH / 2) - 150, 360))
                pygame.display.flip()
                PAUSE = True

                while PAUSE:
                    event = pygame.event.wait()

                    if event.type == KEYDOWN_EVENT and (event.key == R_KEY):
                        PAUSE = False

                        LIVES = 1
                        SPRITES.empty()
                        BRICKS.empty()
                        paddle, bouncer, FONT = set_up(35, 60, 3, [RED, ORANGE, YELLOW])
                    elif event.type == CLOSE_WINDOW:
                        PAUSE = False
                        PLAY = False
                    elif event.type == KEYDOWN_EVENT and (event.key == ESC_KEY or event.key == Q_KEY):
                        PAUSE = False
                        PLAY = False
        if bouncer.rect.y < 40:
            bouncer.velocity[1] = -bouncer.velocity[1]

        if pygame.sprite.collide_mask(bouncer, paddle):
            bouncer.rect.x -= bouncer.velocity[0]
            bouncer.rect.y -= bouncer.velocity[1]
            bouncer.bounce()

        # Handle brick collision
        brick_collisions = pygame.sprite.spritecollide(bouncer, BRICKS, False)
        for b in brick_collisions:
            bouncer.bounce()
            SCORE += 1
            b.kill()
            if len(brick_collisions) == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                SCREEN.blit(text, (int((WIDTH-400) / 2), 300))
                pygame.display.flip()
                pygame.time.wait(3000)
                PLAY = False

        # Drawing
        SCREEN.fill(PALEBLUE)
        pygame.draw.line(SCREEN, WHITE, [0, 30], [WIDTH, 30], 2)
        text = FONT.render("Score: " + str(SCORE), 1, WHITE)
        SCREEN.blit(text, (20, 10))
        text = FONT.render("Lives: " + str(LIVES), 1, WHITE)
        SCREEN.blit(text, (WIDTH - 150, 10))
        SPRITES.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
