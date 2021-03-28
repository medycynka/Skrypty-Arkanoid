from Arkanoid.setup import *
import pygame


def lvl_one() -> None:
    bricks_hp = [1, 1, 1]
    bricks_colors = [gl.RED, gl.ORANGE, gl.YELLOW]
    gl.SPRITES.empty()
    gl.BRICKS.empty()
    gl.PLAY = True
    gl.PAUSE = False

    paddle, bouncer, FONT = set_up(150, 35, 60, 1, bricks_hp, bricks_colors)

    while gl.PLAY:
        # Event handling
        for event in pygame.event.get():
            if event.type == gl.CLOSE_WINDOW:
                gl.PLAY = False
            elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                gl.PLAY = False
            elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
                gl.PAUSE = True
                while gl.PAUSE:
                    event = pygame.event.wait()

                    if event.type == gl.KEYDOWN_EVENT and (event.key == gl.P_KEY):
                        gl.PAUSE = False
                    elif event.type == gl.CLOSE_WINDOW:
                        gl.PAUSE = False
                        gl.PLAY = False
                    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                        gl.PAUSE = False
                        gl.PLAY = False

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[gl.LEFT_A]:
            paddle.move_left(gl.MOVE_AMOUNT)
        if keys[gl.RIGHT_A]:
            paddle.move_right(gl.MOVE_AMOUNT)

        # Updating
        gl.SPRITES.update()

        # Handle ball movement and collisions
        if bouncer.rect.x >= gl.WIDTH - 10:
            bouncer.velocity[0] = -bouncer.velocity[0]
        if bouncer.rect.x <= 0:
            bouncer.velocity[0] = -bouncer.velocity[0]
        if bouncer.rect.y > gl.HEIGHT - 10:
            bouncer.velocity[1] = -bouncer.velocity[1]
            gl.LIVES -= 1

            if gl.LIVES == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, gl.WHITE)
                gl.SCREEN.blit(text, (int((gl.WIDTH - 300) / 2), 300))
                text = FONT.render("Press R to reset or esc/q to quit", 1, gl.WHITE)
                gl.SCREEN.blit(text, (int(gl.WIDTH / 2) - 150, 360))
                pygame.display.flip()
                gl.update_high_scores(gl.SCORE)
                gl.PAUSE = True

                while gl.PAUSE:
                    event = pygame.event.wait()

                    if event.type == gl.KEYDOWN_EVENT and (event.key == gl.R_KEY):
                        gl.PAUSE = False

                        gl.LIVES = 3
                        gl.SCORE = 0
                        gl.SPRITES.empty()
                        gl.BRICKS.empty()
                        paddle, bouncer, FONT = set_up(150, 35, 60, 3, bricks_hp, bricks_colors)
                    elif event.type == gl.CLOSE_WINDOW:
                        gl.PAUSE = False
                        gl.PLAY = False
                    elif event.type == gl.KEYDOWN_EVENT and (event.key == gl.ESC_KEY or event.key == gl.Q_KEY):
                        gl.PAUSE = False
                        gl.PLAY = False
        if bouncer.rect.y < 40:
            bouncer.velocity[1] = -bouncer.velocity[1]

        if pygame.sprite.collide_mask(bouncer, paddle):
            bouncer.rect.x -= bouncer.velocity[0]
            bouncer.rect.y -= bouncer.velocity[1]
            bouncer.bounce()

        # Handle brick collision
        brick_collisions = pygame.sprite.spritecollide(bouncer, gl.BRICKS, False)
        for b in brick_collisions:
            bouncer.bounce()
            b.hp -= 1

            if b.hp == 0:
                gl.SCORE += b.reward
                b.kill()

            if len(gl.BRICKS) == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL 1 COMPLETE", 1, gl.WHITE)
                gl.SCREEN.blit(text, (int((gl.WIDTH - 450) / 2), 300))
                font = pygame.font.Font(None, 34)
                text = font.render("Next level starts in 3 seconds", 1, gl.WHITE)
                gl.SCREEN.blit(text, (int((gl.WIDTH - 300) / 2), 360))
                pygame.display.flip()
                gl.PLAY = False
                gl.LVL1_COMPLETE = True
                gl.update_high_scores(gl.SCORE)
                pygame.time.wait(3000)

        # Drawing
        gl.SCREEN.fill(gl.PALEBLUE)
        pygame.draw.line(gl.SCREEN, gl.WHITE, [0, 30], [gl.WIDTH, 30], 2)
        text = FONT.render("Score: " + str(gl.SCORE), 1, gl.WHITE)
        gl.SCREEN.blit(text, (20, 10))
        text = FONT.render("Lives: " + str(gl.LIVES), 1, gl.WHITE)
        gl.SCREEN.blit(text, (gl.WIDTH - 150, 10))
        gl.SPRITES.draw(gl.SCREEN)

        pygame.display.flip()
        gl.CLOCK.tick(60)
