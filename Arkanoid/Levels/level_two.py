from Arkanoid.Levels.levels_event_manager import *


def lvl_two(start_lives: int, effect: pygame.mixer.Sound) -> Tuple[bool, bool, bool, int, int]:
    bricks_hp = [1, 1, 1, 1]
    bricks_colors = [gl.RED, gl.ORANGE, gl.YELLOW, gl.CYAN]
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    paddle, bouncer, FONT = set_up(125, 35, 60, 4, 3, bricks_hp, bricks_colors, effect)

    return level_main_loop(paddle, bouncer, FONT, start_lives)
