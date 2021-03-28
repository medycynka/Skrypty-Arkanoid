import pygame
from typing import Tuple


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, width: int, height: int, color: Tuple, bg_color: Tuple):
        super().__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_left(self, pixels) -> None:
        if self.rect.x - pixels < 0:
            self.rect.x = 0
        else:
            self.rect.x -= pixels

    def move_right(self, pixels) -> None:
        if self.rect.x + pixels > self.screen_width - self.width:
            self.rect.x = self.screen_width - self.width
        else:
            self.rect.x += pixels
