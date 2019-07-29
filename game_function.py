import pygame
import sys

def initGame(pie, screen, ai_settings):
    screen.fill(ai_settings.bg_color)
    pie.initBlocks()

def update_screen():
    pygame.display.flip()

def check_direction(event):
    k = event.key
    if k == pygame.K_a or k == pygame.K_LEFT or k == pygame.K_s or k == pygame.K_DOWN or k == pygame.K_d \
        or k == pygame.K_RIGHT or k == pygame.K_w or k == pygame.K_UP:
        return True
    return False

def check_key_event(event, pie, ai_settings, screen):
    k = event.key
    if k == pygame.K_q:
        sys.exit()
    elif pie.canMove and check_direction(event):
        pie.canMove = False
        if k == pygame.K_a or k == pygame.K_LEFT:
            pie.updateBlocks(screen, ai_settings, 0, 3, 4, 1, 3)
        elif k == pygame.K_s or k == pygame.K_DOWN:
            pie.updateBlocks(screen, ai_settings, 3, 15, -1, 4, 2)
        elif k == pygame.K_d or k == pygame.K_RIGHT:
            pie.updateBlocks(screen, ai_settings, 12, 15, -4, 1, 1)
        elif k == pygame.K_w or k == pygame.K_UP:
            pie.updateBlocks(screen, ai_settings, 0, 12, 1, 4, 0)

def check_event(pie, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_event(event, pie, ai_settings, screen)
