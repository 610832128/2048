import pygame
from block import Block
from settings import Settings
from pie import Pie
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pie = Pie(screen, ai_settings)
    pygame.display.set_caption("2048")
    gf.initGame(pie, screen, ai_settings)
    gf.update_screen()
    while True:
        gf.check_event(pie, ai_settings, screen)
        #gf.update_screen(screen, ai_settings)

run_game()