"""Основыне функции игры."""
import sys

import pygame

def check_events(ship):
    """Обрабатывает нажатия клавишь и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Переместить корабль вправо.
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и выводит новый экран."""
    # При каждом прохоже цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
