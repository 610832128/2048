import random
from block import Block
import game_function as gf

class Pie():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.blocks = [False] * 16

    def addOneBlock(self):
        tmp0 = random.randint(0, 15)
        tmp = tmp0
        while self.blocks[tmp]:
            tmp = (tmp + 1) % 16
            if tmp == tmp0:
                return None
        x, y = int(tmp / 4), int(tmp % 4)
        topleftX, topLeftY = (x * self.ai_settings.span) + 20, (y * self.ai_settings.span) + 20
        block = Block(self.screen, self.ai_settings, topleftX, topLeftY)
        block.setIdx(tmp)
        self.blocks[block.idx] = block
        return block

    def initBlocks(self):
        num = random.randint(4, 6)
        for idx in range(num):
            block = self.addOneBlock()
            block.drawBlock()

    def updateBlocks(self, screen, ai_settings, min_idx, max_idx, span_idx0, span_idx1):
        isChange = False
        for idx in range(min_idx, max_idx + 1, span_idx1):
            idx0, idx1, idx_empty = idx, idx + span_idx0, idx
            minV, maxV = idx, idx + 3 * span_idx0
            if minV > maxV:
                minV, maxV = maxV, minV
            while minV <= idx1 <= maxV:
                if not self.blocks[idx0]:
                    idx0, idx1 = idx1, idx1 + span_idx0
                elif not self.blocks[idx1]:
                    idx1 = idx1 + span_idx0
                else:
                    if self.blocks[idx0].txt == self.blocks[idx1].txt:
                        isChange = True
                        self.blocks[idx0].txt = str(int(self.blocks[idx0].txt) * 2)
                        self.blocks[idx1] = False
                        if idx0 != idx_empty:
                            self.blocks[idx_empty] = self.blocks[idx0]
                            self.blocks[idx0] = False
                        self.blocks[idx_empty].setIdx(idx_empty)
                        idx0, idx1, idx_empty = idx1 + span_idx0, idx1 + 2 * span_idx0, idx_empty + span_idx0
                    else:
                        if idx0 != idx_empty:
                            tmp = self.blocks[idx0]
                            self.blocks[idx0] = False
                            self.blocks[idx_empty] = tmp
                            self.blocks[idx_empty].setIdx(idx_empty)
                            isChange = True
                        idx0, idx1, idx_empty = idx1, idx1 + span_idx0, idx_empty + span_idx0
            if minV <= idx0 <= maxV and self.blocks[idx0]:
                if idx_empty != idx0:
                    self.blocks[idx_empty] = self.blocks[idx0]
                    self.blocks[idx0] = False
                    isChange = True
                self.blocks[idx_empty].setIdx(idx_empty)
        if isChange == True:
            screen.fill(ai_settings.bg_color)
            block = self.addOneBlock()
            for idx in range(16):
                if self.blocks[idx]:
                    self.blocks[idx].updateBlock()
            gf.update_screen()
