import pygame
from typing import Tuple


class Brick(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, bg_color: Tuple, color: Tuple):
        super().__init__()

        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
