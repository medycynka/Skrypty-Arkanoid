import pygame
from typing import Tuple


class Button(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, font_size: int, font_color: Tuple, bg_color: Tuple, color: Tuple,
                 text: str):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont(None, font_size)
        self.textSurf = self.font.render(text, 1, font_color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width / 2 - W / 2, height / 2 - H / 2])
        self.rect = self.image.get_rect()
