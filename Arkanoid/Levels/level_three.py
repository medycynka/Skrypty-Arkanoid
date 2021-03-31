from Arkanoid.Levels.levels_event_manager import *


def lvl_three(start_lives: int) -> Tuple[bool, bool, bool, int, int]:
    bricks_hp = [1, 1, 3, 1, 1]
    bricks_colors = [gl.RED, gl.ORANGE, gl.YELLOW, gl.CYAN, gl.MAGENTA]
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    paddle, bouncer, FONT = set_up(100, 35, 60, 5, 4, bricks_hp, bricks_colors)

    return level_main_loop(paddle, bouncer, FONT, start_lives)
