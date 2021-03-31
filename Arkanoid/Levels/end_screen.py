import pygame
import Arkanoid.globals as gl
import Arkanoid.button as btn
from typing import Tuple, List


pause = False
end_loop = True
menu = True


def end_screen(curr_score: int, scores: List) -> Tuple[bool, bool]:
    global end_loop
    global menu

    gl.SPRITES.empty()
    gl.BRICKS.empty()
    big_f = pygame.font.Font(None, 80)
    normal_f = pygame.font.Font(None, 34)

    play_btn = btn.Button(250, 50, 34, gl.BLACK, gl.BLACK, gl.WHITE, "Back")
    play_btn.rect.x = 100
    play_btn.rect.y = int(gl.HEIGHT - 100)
    gl.SPRITES.add(play_btn)
    quit_btn = btn.Button(250, 50, 34, gl.BLACK, gl.BLACK, gl.WHITE, "Quit")
    quit_btn.rect.x = int(gl.WIDTH - 250 - 100)
    quit_btn.rect.y = int(gl.HEIGHT - 100)
    gl.SPRITES.add(quit_btn)

    while end_loop:
        for event in pygame.event.get():
            main_loop, end_loop, menu = handle_events(event, play_btn, quit_btn)

        update_screen(big_f, normal_f, curr_score, scores)

    return False, menu


def handle_events(event: pygame.event, back_btn: btn.Button, quit_btn: btn.Button) -> Tuple[bool, bool, bool]:
    global pause

    if event.type == gl.CLOSE_WINDOW:
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
        return False, False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
        pause = True
        pygame.mixer.pause()

        while pause:
            event = pygame.event.wait()

            if event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
                pause = False
                pygame.mixer.unpause()
            elif event.type == gl.CLOSE_WINDOW:
                pause = False

                return False, False, False
            elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                pause = False

                return False, False, False
    elif event.type == gl.CLICK:
        x, y = event.pos

        if back_btn.rect.collidepoint(x, y):
            print("Back")

            return True, False, True
        elif quit_btn.rect.collidepoint(x, y):
            print("Quit")

            return False, False, False

    return True, True, True


def update_screen(bf: pygame.font.Font, nf: pygame.font.Font, curr_score: int, scores: List):
    gl.SPRITES.update()
    gl.SCREEN.fill(gl.PALEBLUE)
    gl.SPRITES.draw(gl.SCREEN)
    text = bf.render("Congratulation!", 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 100))
    text = nf.render("Your score: " + str(curr_score), 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 175))

    text = nf.render("High scores:", 1, gl.WHITE)
    gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 300 - text.get_height() - 10))
    for i in range(len(scores)):
        text = nf.render(f'{i+1}.   {scores[i]}', 1, gl.WHITE)
        gl.SCREEN.blit(text, (int(gl.WIDTH / 2 - text.get_width() / 2), 300 + i * (text.get_height() + 10)))

    pygame.display.flip()
    gl.CLOCK.tick(60)
