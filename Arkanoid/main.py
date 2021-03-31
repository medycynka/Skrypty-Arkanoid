import Arkanoid.Levels.main_menu as mm
import Arkanoid.Levels.level_one as lvl1
import Arkanoid.Levels.level_two as lvl2
import Arkanoid.Levels.level_three as lvl3
import Arkanoid.Levels.level_four as lvl4
import Arkanoid.Levels.level_five as lvl5
import Arkanoid.Levels.end_screen as es
import pygame


if __name__ == '__main__':
    pygame.init()
    main_loop = True
    main_menu = True
    start = True
    lvl1_complete = False
    lvl2_complete = False
    lvl3_complete = False
    lvl4_complete = False
    lvl5_complete = False
    score = 0
    lives = 3

    while main_loop:
        if main_menu:
            lvl1_complete = False
            lvl2_complete = False
            lvl3_complete = False
            lvl4_complete = False
            lvl5_complete = False
            score = 0
            lives = 3
            main_loop, main_menu, start = mm.main_menu()

        if start:
            main_loop, lvl1_complete, main_menu, score, lives = lvl1.lvl_one(lives)

            if lvl1_complete:
                main_loop, lvl2_complete, main_menu, score, lives = lvl2.lvl_two(lives)

            if lvl2_complete:
                main_loop, lvl3_complete, main_menu, score, lives = lvl3.lvl_three(lives)

            if lvl3_complete:
                main_loop, lvl4_complete, main_menu, score, lives = lvl4.lvl_four(lives)

            if lvl4_complete:
                main_loop, lvl5_complete, main_menu, score, lives = lvl5.lvl_five(lives)

            mm.update_high_scores(score)

            if lvl5_complete:
                main_loop, main_menu = es.end_screen(score, mm.HIGH_SCORES)

    mm.save_scores()
    pygame.quit()
