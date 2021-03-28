import pygame
from random import randint
from typing import Tuple


class Ball(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, speed: int, bg_color: Tuple, color: Tuple):
        super().__init__()

        if speed <= 4:
            speed = 4

        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        rand_y = randint(-speed, speed)
        while rand_y == 0:
            rand_y = randint(-speed, speed)
        self.velocity = [randint(2, speed), rand_y]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        rand_y = randint(-self.speed, self.speed)
        while rand_y == 0:
            rand_y = randint(-self.speed, self.speed)
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = rand_y
