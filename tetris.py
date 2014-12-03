# -*- coding: cp936 -*-

import random
from board import Board
from shape import Shape

#global variables
SHAPES = (
        (   ((1,1),     #   [][]
             (1,1)),   #
        ),
        (   ((0,0,0,0),     #
             (1,1,1,1),     # [][][][]
             (0,0,0,0),     #
             (0,0,0,0))),   #   []
        ),
        (   ((0,0,0),     #
             (0,1,1),     #   [][]
             (1,1,0))),
        ),
        (   ((1,1,0),     # [][]
             (0,1,1),     #   [][]
             (0,0,0)),),   #
        ),
        (   ((1,1,1),     # [][][]
             (1,0,0),     # []
             (0,0,0)),),   #
        ),
        (   ((0,0,0,0),     #
             (1,1,1,0),     # [][][]
             (0,0,1,0),     #     []
             (0,0,0,0),),   #
            ((0,1,1,0),     #   [][]
             (0,1,0,0),     #   []
             (0,1,0,0),     #   []
             (0,0,0,0),),   #
            ((1,0,0,0),     # []
             (1,1,1,0),     # [][][]
             (0,0,0,0),     #
             (0,0,0,0),),   #
            ((0,1,0,0),     #   []
             (0,1,0,0),     #   []
             (1,1,0,0),     # [][]
             (0,0,0,0),),   #
        ),
        (   ((0,0,0,0),     #
             (1,1,1,0),     # [][][]
             (0,1,0,0),     #   []
             (0,0,0,0),),   #
            ((0,1,0,0),     #   []
             (0,1,1,0),     #   [][]
             (0,1,0,0),     #   []
             (0,0,0,0),),   #
            ((0,1,0,0),     #   []
             (1,1,1,0),     # [][][]
             (0,0,0,0),     #
             (0,0,0,0),),   #
            ((0,1,0,0),     #   []
             (1,1,0,0),     # [][]
             (0,1,0,0),     #   []
             (0,0,0,0),),   #
        ),
    )

    
class Tetris(object):
    W = 12          # board区域横向多少个格子
    H = 20          # 纵向多少个格子
    TILEW = 20      # 每个格子的高/宽的像素数
    START = (100, 20) # board在屏幕上的位置
    SPACE = 1000    # 方块在多少毫秒内会落下(现在是level 1)
 
    def __init__(self, screen):
        self.stat = "game"
        self.WIDTH = self.TILEW * self.W
        self.HEIGHT = self.TILEW * self.H
        self.screen = screen
        # board数组，空则为None
        self.board = []
        for i in xrange(self.H):
            line = [ None ] * self.W
            self.board.append(line)
        # 一些需要显示的信息
        self.level = 1
        self.killed = 0
        self.score = 0
        # 多少毫秒后会落下，当然在init里肯定是不变的(level总是一）
        self.time = self.SPACE * 0.8 ** (self.level - 1)
        # 这个保存自从上一次落下后经历的时间
        self.elapsed = 0
        # used for judge pressed firstly or for a  long time
        self.pressing = 0
        # 当前的shape
        self.shape = Shape(self.START,
                (self.WIDTH, self.HEIGHT), (self.W, self.H))
        # shape需要知道周围世界的事情
        self.shape.set_board(self.board)
        # 这个是“世界”的“快照”
        self.board_image = pygame.Surface((self.WIDTH, self.HEIGHT))
        # 做一些初始化的绘制
        self.screen.blit(pygame.image.load(
            util.file_path("background.jpg")).convert(), (0, 0))
        self.display_info()

 
    def update(self, elapse):
        # 在游戏阶段，每次都会调用这个，用来接受输入，更新画面
        pass
 
    def move(self, u, d, l, r):
        # 控制当前方块的状态
        pass
 
    def check_line(self):
        # 判断已经落下方块的状态，然后调用kill_line
        pass
 
    def kill_line(self, filled=[]):
        # 删除填满的行，需要播放个消除动画
        pass
 
    def get_score(self, num):
        # 计算得分
       pass
 
    def add_to_board(self):
        # 将触底的方块加入到board数组中
       pass
 
    def create_board_image(self):
        # 创造出一个稳定方块的图像
        pass
 
    def next(self):
        # 产生下一个方块
        pass
 
    def draw(self):
        # 把当前状态画出来
        pass
 
    def display_info(self):
        # 显示各种信息（分数，等级等），调用下面的_display***
        pass
 
    def _display_score(self):
        pass
 
    def _display_next(self):
        pass
 
    def game_over(self):
        # 游戏结束
        pass




def spawnShape():
    global SHAPES
    return SHAPES[1]#random.randint(0, 6)]



def movedown(b):
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()
    b.moveDown()

s1 = Shape(spawnShape())
'''
print 'before rotate:'
s1.draw(None)

s1.rotate()
print 'after 1st rotate:'
s1.draw(None)

s1.rotate()
print 'after 2nd rotate:'
s1.draw(None)

s1.rotate()
print 'after 3th rotate:'
s1.draw(None)

s1.rotate()
print 'after 4th rotate:'
s1.draw(None)
'''
s2 = Shape(spawnShape())
b = Board(s1,s2)
b.draw()
movedown(b)
#b.rotate()

print '------------------------------------------'
b.draw()
