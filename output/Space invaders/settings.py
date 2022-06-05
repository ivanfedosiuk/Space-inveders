class Settings:
    """Клас для збереження налаштувань"""

    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (255, 255, 255)

        # Налаштування кулі
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 220, 220)
        self.bullets_alowed = 3

        # Налаштування корабля
        self.ship_limit = 2

        # Налаштування прибульця
        self.fleet_drop_speed = 10

        # як швидко гра прискорюється
        self.speed_up = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.bullet_speed = 1.0
        self.ship_speed = 1.5
        self.alien_speed = 2.0
        self.fleet_direction = 1
        self.alien_point = 50


    def increase_speed(self):
        self.bullet_speed *= self.speed_up
        self.ship_speed *= self.speed_up
        self.alien_speed *= self.speed_up
        self.alien_point = int(self.alien_point * self.score_scale)

    def hard_mod_on(self):
        self.speed_up *= 2