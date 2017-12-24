"""Класс для хранения настроек игры"""

class Settings():
    """хранит настройки игры"""

    def __init__(self):
        """Инициализурет настройки игры"""
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (115, 104, 255)
        #настройки корабля
        self.ship_speed_factor = 1.5
