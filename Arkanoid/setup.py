import globals as gl
from typing import List, Tuple
import player
import ball
import brick
import pygame


def set_up(paddle_width: int, start_x: int, start_y: int, col: int, ball_speed: int, hps: List, colors: List,
           effect: pygame.mixer.Sound) -> Tuple[player.Player, ball.Ball, pygame.font.Font]:
    pygame.init()
    pygame.display.set_caption(gl.TITLE)
    f = pygame.font.Font(None, 34)

    p = player.Player(gl.WIDTH, gl.HEIGHT, paddle_width, 10, gl.LIGHTBLUE, gl.BLACK)
    p.rect.x = int((gl.WIDTH - 100) / 2)
    p.rect.y = gl.HEIGHT - 40

    bo = ball.Ball(10, 10, ball_speed, gl.BLACK, gl.WHITE, effect)
    bo.rect.x = int((gl.WIDTH - 100) / 2)
    bo.rect.y = gl.HEIGHT - 55

    generate_bricks(start_x, start_y, col, hps, colors)

    gl.SPRITES.add(p)
    gl.SPRITES.add(bo)

    return p, bo, f


def generate_bricks(start_x: int, start_y: int, col: int, hps: List, colors: List):
    if col != len(colors) or col != len(hps):
        raise ValueError("Number of columns and length of color's/hps list must be the same!")

    line_count = int((gl.WIDTH - (2 * 5 - gl.SPACING)) / (gl.BRICK_WIDTH + gl.SPACING))
    for j in range(col):
        for i in range(line_count):
            br = brick.Brick(gl.BRICK_WIDTH, gl.BRICK_HEIGHT, hps[j], gl.BLACK, colors[j])
            br.rect.x = start_x + i * (gl.BRICK_WIDTH + gl.SPACING)
            br.rect.y = start_y + j * (gl.BRICK_HEIGHT + gl.SPACING)
            gl.SPRITES.add(br)
            gl.BRICKS.add(br)
