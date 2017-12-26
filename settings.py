"""Класс для хранения настроек игры"""

class Settings():
    """хранит настройки игры"""

    def __init__(self):
        """Инициализурет статические настройки игры"""
        self.screen_width = 700
        self.screen_height = 450
        self.bg_color = (50, 90, 70)
        #настройки корабля
        self.ship_limit = 3
        #параметры пули
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 50, 25, 25
        self.bullets_allowed = 3
        # aliens settings
        self.fleet_drop_speed = 10
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.iniialize_dynamic_settings()


    def iniialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
