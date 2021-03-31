import pygame
import Arkanoid.globals as gl
import Arkanoid.button as btn
from typing import Tuple
import os


pause = False
HIGH_SCORES = [0, 0, 0, 0, 0, 0, 0]


def main_menu() -> Tuple[bool, bool, bool]:
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    main_loop = False
    menu = True
    start = False
    menu_title = "Arkanoid"
    author = "by Szymon Peszek"
    big_f = pygame.font.Font(None, 80)
    normal_f = pygame.font.Font(None, 34)

    play_btn = btn.Button(250, 50, 34, gl.BLACK, gl.BLACK, gl.WHITE, "Play")
    play_btn.rect.x = int(gl.WIDTH / 2) - 125
    play_btn.rect.y = int(gl.HEIGHT / 3) + int(gl.HEIGHT / 6)
    gl.SPRITES.add(play_btn)
    quit_btn = btn.Button(250, 50, 34, gl.BLACK, gl.BLACK, gl.WHITE, "Quit")
    quit_btn.rect.x = int(gl.WIDTH / 2) - 125
    quit_btn.rect.y = int(gl.HEIGHT / 3) * 2
    gl.SPRITES.add(quit_btn)

    while menu:
        for event in pygame.event.get():
            main_loop, menu, start = handle_events(event, play_btn, quit_btn)

        update_screen(big_f, menu_title, normal_f, author)

    return main_loop, menu, start


def handle_events(event: pygame.event, play_btn: btn.Button, quit_btn: btn.Button) -> Tuple[bool, bool, bool]:
    global pause

    if event.type == gl.CLOSE_WINDOW:
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
        pause = True

        while pause:
            event = pygame.event.wait()

            if event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
                pause = False
            elif event.type == gl.CLOSE_WINDOW:
                pause = False

                return False, False, False
            elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                pause = False

                return False, False, False
    elif event.type == gl.CLICK:
        x, y = event.pos

        if play_btn.rect.collidepoint(x, y):
            print("Play")

            return True, False, True
        elif quit_btn.rect.collidepoint(x, y):
            print("Quit")

            return False, False, False

    return True, True, True


def update_screen(bf: pygame.font.Font, title: str, nf: pygame.font.Font, author: str):
    gl.SPRITES.update()
    gl.SCREEN.fill(gl.PALEBLUE)
    gl.SPRITES.draw(gl.SCREEN)
    text = bf.render(title, 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 100))
    text = nf.render(author, 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 175))
    text = nf.render("Current high score: " + str(HIGH_SCORES[0]), 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 300))

    pygame.display.flip()
    gl.CLOCK.tick(60)


def init_high_scores() -> None:
    if not os.path.isfile('scores/high_scores.txt'):
        return

    global HIGH_SCORES

    HIGH_SCORES = [0, 0, 0, 0, 0, 0, 0]

    with open('scores/high_scores.txt', 'r') as file:
        for i in range(len(HIGH_SCORES)):
            HIGH_SCORES[i] = int(file.readline().strip())


def update_high_scores(score: int) -> None:
    for i in range(len(HIGH_SCORES)):
        if score > HIGH_SCORES[i]:
            HIGH_SCORES[i] = score
            return


def save_scores() -> None:
    with open('scores/high_scores.txt', 'w') as file:
        for i in range(len(HIGH_SCORES)):
            file.write(f'{HIGH_SCORES[i]}\n')

