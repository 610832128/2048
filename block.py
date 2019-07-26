import pygame

class Block():
    def __init__(self, screen, ai_settings, topleftX, topleftY):
        self.screen = screen
        self.color = (0, 60, 60)
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, ai_settings.blockWidth, ai_settings.blockHeight)
        self.rect.topleft = (topleftX, topleftY)
        self.idx = -1
        self.text_color = (255, 255, 255)
        self.txt = '2'
        self.font = pygame.font.SysFont(None, 48)
        self.prep_msg(self.txt)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def updateBlock(self):
        x, y = int(self.idx / 4), int(self.idx % 4)
        topleftX, topLeftY = (x * self.ai_settings.span) + 20, (y * self.ai_settings.span) + 20
        self.rect.topleft = (topleftX, topLeftY)
        self.prep_msg(self.txt)
        self.drawBlock()

    def setIdx(self, idx):
        self.idx = idx

    def setText(self, txt):
        self.txt = txt

    def drawBlock(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
