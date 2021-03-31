from Arkanoid.setup import *
import pygame
from typing import Tuple


pause = False
play = True
main_loop = True
lvl_complete = False
back_to_menu = False
score = 0
lives = 0


def level_main_loop(paddle: player.Player, bouncer: ball.Ball, f: pygame.font.Font, curr_lives: int = 3,
                    reset_score: bool = False) -> Tuple[bool, bool, bool, int, int]:
    global pause
    global play
    global main_loop
    global lvl_complete
    global back_to_menu
    global score
    global lives

    pause = False
    play = True
    main_loop = True
    lvl_complete = False
    back_to_menu = False
    lives = curr_lives

    if reset_score:
        score = 0

    while play:
        # Event handling
        for event in pygame.event.get():
            main_loop, play = handle_events(event)

            if not play:
                return main_loop, lvl_complete, back_to_menu, score, lives
        # Handle movement
        handle_movement(paddle)

        # Updating
        gl.SPRITES.update()

        # Handle ball movement and collisions
        main_loop, play, back_to_menu = handle_ball(paddle, bouncer, f)
        if not play:
            return main_loop, lvl_complete, back_to_menu, score, lives

        # Handle brick collision
        play, lvl_complete = handle_collision(bouncer)
        if not play:
            return main_loop, lvl_complete, back_to_menu, score, lives

        # Drawing
        update_screen(f)

    return main_loop, lvl_complete, back_to_menu, score, lives


def handle_events(event: pygame.event) -> Tuple[bool, bool]:
    if event.type == gl.CLOSE_WINDOW:
        return False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
        return False, False
    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
        return pause_game()

    return True, True


def pause_game() -> Tuple[bool, bool]:
    global pause

    pause = True
    while pause:
        event = pygame.event.wait()

        if event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
            pause = False
        elif event.type == gl.CLOSE_WINDOW:
            pause = False

            return False, False
        elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
            pause = False

            return False, False

    return True, True


def handle_movement(paddle: player.Player) -> None:
    keys = pygame.key.get_pressed()
    if keys[gl.LEFT_A]:
        paddle.move_left(gl.MOVE_AMOUNT)
    if keys[gl.RIGHT_A]:
        paddle.move_right(gl.MOVE_AMOUNT)


def handle_ball(paddle: player.Player, bouncer: ball.Ball, f: pygame.font.Font) -> Tuple[bool, bool, bool]:
    global pause
    global lives

    if bouncer.rect.x >= gl.WIDTH - 10:
        bouncer.velocity[0] = -bouncer.velocity[0]
    if bouncer.rect.x <= 0:
        bouncer.velocity[0] = -bouncer.velocity[0]
    if bouncer.rect.y > gl.HEIGHT - 10:
        bouncer.velocity[1] = -bouncer.velocity[1]
        lives -= 1

        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, gl.WHITE)
            gl.SCREEN.blit(text, (int((gl.WIDTH - 300) / 2), 300))
            text = f.render("Press R to reset or esc/q to quit", 1, gl.WHITE)
            gl.SCREEN.blit(text, (int(gl.WIDTH / 2) - 150, 360))
            pygame.display.flip()
            pause = True

            while pause:
                event = pygame.event.wait()

                if event.type == gl.KEYDOWN_EVENT and (event.key == gl.R_KEY):
                    pause = False

                    return True, False, True
                elif event.type == gl.CLOSE_WINDOW:
                    pause = False

                    return False, False, False
                elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                    pause = False

                    return False, False, False
    if bouncer.rect.y < 40:
        bouncer.velocity[1] = -bouncer.velocity[1]

    if pygame.sprite.collide_mask(bouncer, paddle):
        bouncer.rect.x -= bouncer.velocity[0]
        bouncer.rect.y -= bouncer.velocity[1]
        bouncer.bounce()

    return True, True, True


def handle_collision(bouncer: ball.Ball) -> Tuple[bool, bool]:
    global score
    p, c = True, False

    for b in pygame.sprite.spritecollide(bouncer, gl.BRICKS, False):
        bouncer.bounce()
        b.hp -= 1

        if b.hp == 0:
            score += b.reward
            b.kill()

        if len(gl.BRICKS) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL 1 COMPLETE", 1, gl.WHITE)
            gl.SCREEN.blit(text, (int((gl.WIDTH - 450) / 2), 300))
            font = pygame.font.Font(None, 34)
            text = font.render("Next level starts in 3 seconds", 1, gl.WHITE)
            gl.SCREEN.blit(text, (int((gl.WIDTH - 300) / 2), 360))
            pygame.display.flip()
            p = False
            c = True
            pygame.time.wait(3000)

    return p, c


def update_screen(f: pygame.font.Font) -> None:
    gl.SCREEN.fill(gl.PALEBLUE)
    pygame.draw.line(gl.SCREEN, gl.WHITE, [0, 30], [gl.WIDTH, 30], 2)
    text = f.render("Score: " + str(score), 1, gl.WHITE)
    gl.SCREEN.blit(text, (20, 10))
    text = f.render("Lives: " + str(lives), 1, gl.WHITE)
    gl.SCREEN.blit(text, (gl.WIDTH - 150, 10))
    gl.SPRITES.draw(gl.SCREEN)

    pygame.display.flip()
    gl.CLOCK.tick(60)
