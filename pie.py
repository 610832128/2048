import random
from block import Block
import game_function as gf
import time

class Pie():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.blocks = [False] * 16
        self.moveBlockCount = 0
        self.canMove = True
        self.list = [ [0] * 16 for i in range(2)]
        self.dire = -1
        for idx in range(0, 16):
            self.list[0][idx] = idx
            self.list[1][idx] = 15 - idx

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
        self.blocks[tmp] = block
        count = random.randint(1, 4)
        #if count >= 3:
        #    self.blocks[tmp].txt = '4'
        return block

    def initBlocks(self):
        num = random.randint(4, 6)
        for idx in range(num):
            block = self.addOneBlock()
            block.drawBlock()

    def updateMoveBlocks(self, oldIdx):
        block = self.blocks[oldIdx]
        if self.blocks[oldIdx].moveCount == 0:
            self.moveBlockCount -= 1
            if block.moveType == 1 and self.blocks[block.targetIdx] != False:
                block.txt = str(int(block.txt) * 2)
            block.setIdx(block.targetIdx)
            self.blocks[block.idx] = block
            self.blocks[oldIdx] = False
        self.blocks[block.idx].updateShow()

    def moveBlocks(self):
        if self.moveBlockCount == 0:
            return
        self.screen.fill(self.ai_settings.bg_color)
        no = -1
        if self.dire in [0, 3]:
            no = 0
        else:
            no = 1
        for idx in self.list[no]:
            if self.blocks[idx]:
                if self.blocks[idx].moveCount > 0:
                    self.blocks[idx].moveBlock()
                    self.updateMoveBlocks(idx)
                else:
                    self.blocks[idx].updateShow()
        gf.update_screen()
        if self.moveBlockCount == 0:
            time.sleep(0.5)
            block = self.addOneBlock()
            block.drawBlock()
            gf.update_screen()
            self.canMove = True


    def updateBlocks(self, screen, ai_settings, min_idx, max_idx, span_idx0, span_idx1, dire):
        self.dire = dire
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
                        if idx0 != idx_empty:
                            self.blocks[idx0].set_move(idx_empty, dire, 1)
                            self.moveBlockCount += 1
                        self.blocks[idx1].set_move(idx_empty, dire, 1)
                        self.moveBlockCount += 1
                        idx0, idx1, idx_empty = idx1 + span_idx0, idx1 + 2 * span_idx0, idx_empty + span_idx0
                    else:
                        if idx0 != idx_empty:
                            self.blocks[idx0].set_move(idx_empty, dire, 2)
                            self.moveBlockCount += 1
                        idx0, idx1, idx_empty = idx1, idx1 + span_idx0, idx_empty + span_idx0
            if minV <= idx0 <= maxV and self.blocks[idx0]:
                if idx_empty != idx0:
                    self.blocks[idx0].set_move(idx_empty, dire, 2)
                    self.moveBlockCount += 1
