"""Класс для хранения настроек игры"""

class Settings():
    """хранит настройки игры"""

    def __init__(self):
        """Инициализурет настройки игры"""
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (70, 50, 90)
        #настройки корабля
        self.ship_speed_factor = 1.5
        #параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 150, 60, 60
        self.bullets_allowed = 3
