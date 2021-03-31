from Arkanoid.Levels.levels_event_manager import *


def lvl_four(start_lives: int, effect: pygame.mixer.Sound) -> Tuple[bool, bool, bool, int, int]:
    bricks_hp = [1, 2, 2, 3, 3]
    bricks_colors = [gl.RED, gl.ORANGE, gl.YELLOW, gl.CYAN, gl.MAGENTA]
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    paddle, bouncer, FONT = set_up(75, 35, 60, 5, 4, bricks_hp, bricks_colors, effect)

    return level_main_loop(paddle, bouncer, FONT, start_lives)

