"""запуск основного цикла игры"""
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Запуск основного цикла игры."""

    # Инициализация pygame, settings  объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()
