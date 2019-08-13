import pygame
from block import Block
from settings import Settings
from pie import Pie
import game_function as gf

def start_game(screen, ai_settings):
    pie = Pie(screen, ai_settings)
    gf.initGame(pie, screen, ai_settings)
    gf.update_screen()
    while True:
        gf.check_event(pie, ai_settings, screen)
        pie.moveBlocks()

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("2048")
    start_game(screen, ai_settings)

run_game()
print("asdfad")
print("jlksdfjklsdfjklfdskjl")
print("122")