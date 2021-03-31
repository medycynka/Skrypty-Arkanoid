from Arkanoid.Levels.levels_event_manager import *


def lvl_one(start_lives: int) -> Tuple[bool, bool, bool, int, int]:
    bricks_hp = [1, 1, 1]
    bricks_colors = [gl.RED, gl.ORANGE, gl.YELLOW]
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    paddle, bouncer, FONT = set_up(150, 35, 60, 3, 2, bricks_hp, bricks_colors)

    return level_main_loop(paddle, bouncer, FONT, start_lives, True)
