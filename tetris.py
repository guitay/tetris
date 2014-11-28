# -*- coding: cp936 -*-

import random

#global variables
SHAPES = (\
           ((0,1,0,0),\
             (0,1,0,0),\
            (0,1,0,0),\
            (0,1,0,0)),\
           ((0,1,0),\
             (1,1,0),\
            (0,1,0)\
            ),\
            ((1,1),\
             (1,1)\
             ),\
            ((0,0,0),\
             (1,1,1),\
             (1,0,0)\
             ),\
            ((0,0,0),\
             (1,1,1),\
             (0,0,1)\
             ),\
            ((0,1,0),\
             (1,1,0),\
             (1,0,0)\
             ),\
            ((1,0,0),\
             (1,1,0),\
             (0,1,0)\
             )\
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

class Shape():
    # shape是画在一个矩阵上面的
    # 因为我们有不同的模式，所以矩阵的信息也要详细给出
    SHAPEW = 4    # 这个是矩阵的宽度
    SHAPEH = 4    # 这个是高度
    SHAPES = ()
    COLORS = ((0xcc, 0x66, 0x66), # 各个shape的颜色
        )
 
    def __init__(self, board_start, (board_width, board_height), (w, h)):
        self.start = board_start
        self.W, self.H = w, h           # board的横、纵的tile数
        self.length = board_width / w   # 一个tille的长宽(正方形)
        self.x, self.y = 0, 0     # shape的起始位置
        self.index = 0          # 当前shape在SHAPES内的索引
        self.indexN = 0         # 下一个shape在SHAPES内的索引
        self.subindex = 0       # shape是在怎样的一个朝向
        self.shapes = []        # 记录当前shape可能的朝向
        self.color = ()
        self.shape = None
        # 这两个Surface用来存放当前、下一个shape的图像
        self.image = pygame.Surface(
                (self.length * self.SHAPEW, self.length * self.SHAPEH),
                SRCALPHA, 32)
        self.image_next = pygame.Surface(
                (self.length * self.SHAPEW, self.length * self.SHAPEH),
                SRCALPHA, 32)
        self.board = []         # 外界信息
        self.new()            # let's dance!
 
    def set_board(self, board):
        # 接受外界状况的数组
        pass
 
    def new(self):
        # 新产生一个方块
        # 注意这里其实是新产生“下一个”方块，而马上要落下的方块则
        # 从上一个“下一个”方块那里获得
        pass
 
    def rotate(self):
        # 翻转
        pass
 
    def move(self, r, c):
        # 左右下方向的移动
        pass
 
    def check_legal(self, r=0, c=0):
        # 用在上面的move判断中，“这样的移动”是否合法（如是否越界）
        # 合法才会实际的动作
        pass
 
    def at_bottom(self):
        # 是否已经不能再下降了
        pass
 
    def draw_current_shape(self):
        # 绘制当前shhape的图像
        pass
    def draw_next_shape(self):
        # 绘制下一个shape的图像
        pass
    def _draw_shape(self, surface, shape, color):
        # 上两个方法的支援方法
        # 注意这里的绘制是绘制到一个surface中方便下面的draw方法blit
        # 并不是画到屏幕上
        pass
 
    def draw(self, screen):
        # 更新shape到屏幕上
        pass

def spawnShape():
    global SHAPES
    return SHAPES[random.randint(0, 6)]

def printShape(shape):
    x = len(shape)
    print '\n'
    for i in range(x):
        print shape[i]
            
print printShape(spawnShape())
print printShape(spawnShape())
print printShape(spawnShape())
print printShape(spawnShape())
print printShape(spawnShape())
print printShape(spawnShape())
print printShape(spawnShape())
