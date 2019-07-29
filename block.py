import pygame
import math

class Block():
    def __init__(self, screen, ai_settings, topleftX, topleftY):
        self.screen = screen
        self.color = (0, 60, 60)
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, ai_settings.blockWidth, ai_settings.blockHeight)
        self.rect.topleft = (topleftX, topleftY)
        self.idx = -1
        self.targetIdx = -1
        self.text_color = (255, 255, 255)
        self.txt = '2'
        self.font = pygame.font.SysFont(None, 48)
        self.prep_msg(self.txt)
        self.moveCount = 0
        self.moveDire = -1
        self.moveType = -1

    def set_move(self, idx, moveDire, moveType):
        self.moveDire = moveDire
        self.moveType = moveType
        self.targetIdx = idx
        x, y = int(idx / 4), int(idx % 4)
        topleftX, topLeftY = (x * self.ai_settings.span) + 20, (y * self.ai_settings.span) + 20
        self.moveCount = int(math.fabs(self.rect.topleft[0] - topleftX + self.rect.topleft[1] - topLeftY) / self.ai_settings.speed)

    def updateShow(self):
        self.prep_msg(self.txt)
        self.drawBlock()

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def moveBlock(self):
        topLeftX = self.rect.topleft[0] + self.ai_settings.direX[self.moveDire] * self.ai_settings.speed
        topLeftY = self.rect.topleft[1] + self.ai_settings.direY[self.moveDire] * self.ai_settings.speed
        self.rect.topleft = (topLeftX, topLeftY)
        self.moveCount -= 1


    def setIdx(self, idx):
        self.idx = idx

    def setText(self, txt):
        self.txt = txt

    def drawBlock(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
