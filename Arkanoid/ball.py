import pygame
from random import randint
from typing import Tuple


class Ball(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, speed: int, bg_color: Tuple, color: Tuple, effect: pygame.mixer.Sound):
        super().__init__()

        if speed <= 0:
            speed = 2

        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [speed, -speed]
        self.bounce_effect = effect

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        y_dir = randint(0, 9)

        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1] if y_dir < 5 else self.velocity[0]
        self.bounce_effect.play()
