class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Инициализирует статистику, меняющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        with open('save/record.txt', 'r') as f_obj:
            hight_score = f_obj.read()
        return int(hight_score)
