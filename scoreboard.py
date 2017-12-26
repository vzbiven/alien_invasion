import pygame.font
class Scoreboard:
    """Класс для вывода игровой информации"""
    def __init__(self, ai_settings, screen, stats):
        """Инициавлизирует атрибуты подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Настройка шрифта для вывода счета
        self.text_color = (170, 170, 170)
        self.font = pygame.font.SysFont(None, 24)
        # Подготовка исходного изображения
        self.prep_score()


    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                           self.text_color, self.ai_settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10


    def show_score(self):
        """Выводит счет на экран"""
        self.screen.blit(self.score_image, self.score_rect)
