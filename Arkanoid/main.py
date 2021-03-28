import globals as gl
import Arkanoid.Levels.level_one as lvl1
import Arkanoid.Levels.level_two as lvl2
import Arkanoid.Levels.level_three as lvl3
import Arkanoid.Levels.level_four as lvl4
import Arkanoid.Levels.level_five as lvl5
import pygame


if __name__ == '__main__':
    lvl1.lvl_one()

    if gl.LVL1_COMPLETE:
        lvl2.lvl_two()
    elif gl.LVL2_COMPLETE:
        lvl3.lvl_three()
    elif gl.LVL3_COMPLETE:
        lvl4.lvl_four()
    elif gl.LVL4_COMPLETE:
        lvl5.lvl_five()
    elif gl.LVL5_COMPLETE:
        # Credits
        pass

    pygame.quit()
