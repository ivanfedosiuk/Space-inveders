import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Клас для керування корaблем"""

    def __init__(self, ai_game, ship_image):
        '''Ініціалізувати корабель та задати йому початкову позицію'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        '''Завантажити зображення та отpимати його rect'''
        self.image = pygame.image.load(ship_image)
        self.rect = self.image.get_rect()

        # Створювати кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Індикатори руху
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Оновити поточну позицію корабля на основі індикатора руху'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

