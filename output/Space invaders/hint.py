import pygame.font


class Hint:
    ''''Клас для підсказки '''
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midbottom = self.screen_rect.midbottom

    def draw_hint(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)