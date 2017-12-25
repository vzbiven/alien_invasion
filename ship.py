"""Класс описывающий корабль игрока"""

import pygame

class Ship:
    """Корабль игрока"""

    def __init__(self, ai_settings, screen):
        """Инициалзирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        #повернуть корабль на 90 градусов
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у левого края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        #сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centery)
        # Флаги перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        #Движение вверх
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        #Движение вниз
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        #бновление атрибута rect на основании self.center
        self.rect.centery = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
