import pygame
from pygame.sprite import Sprite


class Logo(Sprite):
    """Клас для створення логотипу"""
    def __init__(self, logo_location):
        super().__init__()
        self.image = pygame.image.load("images/logo.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = logo_location


