import pygame
import Arkanoid.globals as gl
import Arkanoid.button as btn
from typing import Tuple
import os


pause = False
HIGH_SCORES = [0, 0, 0, 0, 0, 0, 0]
SONG_END = pygame.USEREVENT
SONG_ID = 0
SOUNDTRACK = ['Music/19-2000 [8 Bit Universe Tribute to Gorillaz].mp3',
              'Music/On Melancholy Hill [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3',
              'Music/Feel Good Inc. (2019 Remaster) [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3',
              'Music/Strobelite [8 Bit Tribute to Gorillaz] - 8 Bit Universe (WARNING Epileptics beware).mp3',
              'Music/Andromeda [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3',
              'Music/Clint Eastwood [8 Bit Cover Tribute to Gorillaz] - 8 Bit Universe.mp3']


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
    controls_font = pygame.font.Font(None, 28)

    play_btn = btn.Button(250, 50, 34, gl.PALEBLUE, gl.BLACK, gl.LIGHT_GREY, "Play")
    play_btn.rect.center = (int(gl.WIDTH / 2), int(gl.HEIGHT / 4) * 2 + int(gl.HEIGHT / 8) - 25)
    gl.SPRITES.add(play_btn)
    quit_btn = btn.Button(250, 50, 34, gl.PALEBLUE, gl.BLACK, gl.LIGHT_GREY, "Quit")
    quit_btn.rect.center = (int(gl.WIDTH / 2), int(gl.HEIGHT / 4) * 3 - 50)
    gl.SPRITES.add(quit_btn)

    while menu:
        for event in pygame.event.get():
            main_loop, menu, start = handle_events(event, play_btn, quit_btn)

        update_screen(big_f, menu_title, normal_f, author, controls_font)

    return main_loop, menu, start


def handle_events(event: pygame.event, play_btn: btn.Button, quit_btn: btn.Button) -> Tuple[bool, bool, bool]:
    global pause

    if event.type == gl.CLOSE_WINDOW:
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
        pause = True
        pygame.mixer.music.pause()

        while pause:
            event = pygame.event.wait()

            if event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
                pause = False
                pygame.mixer.music.unpause()
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
    elif event.type == SONG_END:
        queue_next_song()

    return True, True, True


def update_screen(bf: pygame.font.Font, title: str, nf: pygame.font.Font, author: str, cf: pygame.font.Font):
    gl.SPRITES.update()
    gl.SCREEN.fill(gl.PALEBLUE)
    gl.SPRITES.draw(gl.SCREEN)
    text = bf.render(title, 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 100))
    text = nf.render(author, 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 175))
    text = nf.render("Current high scores:", 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 275))
    text = nf.render("1.   " + str(HIGH_SCORES[0]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 275 + text.get_height() + 10))
    text = nf.render("2.   " + str(HIGH_SCORES[1]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - 2 * text.get_width() - 10), 275 + 2 * (text.get_height() + 10)))
    text = nf.render("3.   " + str(HIGH_SCORES[2]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 + text.get_width() + 10), 275 + 2 * (text.get_height() + 10)))
    text = nf.render("4.   " + str(HIGH_SCORES[3]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - 2 * (2 * text.get_width() - 10) - 10), 275 + 3 * (text.get_height() + 10)))
    text = nf.render("5.   " + str(HIGH_SCORES[4]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - 2 * text.get_width() + 10), 275 + 3 * (text.get_height() + 10)))
    text = nf.render("6.   " + str(HIGH_SCORES[5]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 + text.get_width() - 10), 275 + 3 * (text.get_height() + 10)))
    text = nf.render("7.   " + str(HIGH_SCORES[6]), 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 + 2 * (text.get_width() + 10) + 10), 275 + 3 * (text.get_height() + 10)))
    text = nf.render("CONTROLS", 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), int(3 * gl.HEIGHT / 4 + text.get_height())))
    text = cf.render("< l_arrow, r_arrow > - paddle movement", 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), int(3 * gl.HEIGHT / 4 + text.get_height() + 35)))
    text = cf.render("p - pause/unpause", 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), int(3 * gl.HEIGHT / 4 + text.get_height() + 65)))
    text = cf.render("q/esc - quit game", 1, gl.LIGHT_GREY)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), int(3 * gl.HEIGHT / 4 + text.get_height() + 95)))

    pygame.display.flip()
    gl.CLOCK.tick(60)


def init_high_scores() -> None:
    if not os.path.isfile('Scores/high_scores.txt'):
        return

    global HIGH_SCORES

    HIGH_SCORES = []

    with open('Scores/high_scores.txt', 'r') as file:
        for i in range(7):
            HIGH_SCORES.append(int(file.readline().strip()))


def update_high_scores(score: int) -> None:
    for i in range(len(HIGH_SCORES)):
        if score > HIGH_SCORES[i]:
            HIGH_SCORES[i] = score
            return


def save_scores() -> None:
    with open('Scores/high_scores.txt', 'w') as file:
        for i in range(len(HIGH_SCORES)):
            file.write(f'{HIGH_SCORES[i]}\n')


def set_up_music() -> None:
    pygame.mixer.music.load(SOUNDTRACK[SONG_ID])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.play()


def queue_next_song() -> None:
    global SONG_ID

    SONG_ID += 1
    if SONG_ID == len(SOUNDTRACK):
        SONG_ID = 0

    pygame.mixer.music.load(SOUNDTRACK[SONG_ID])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.play()
