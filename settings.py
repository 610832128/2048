class Settings():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.blockWidth = 100
        self.blockHeight = 100
        self.bg_color = (255, 255, 255)
        self.span = 120
        #0zheng,1dao,2dao,3zheng
        self.direX = [0, 1, 0, -1]
        self.direY = [-1, 0, 1, 0]
        self.speed = 120
