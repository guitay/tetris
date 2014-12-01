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
    COLORS = ((0xcc, 0x66, 0x66), # 各个shape的颜色
        )

    def __init__(self,shape):
        self.SHAPE_WIDTH = len(shape) #矩阵的宽度
        self.SHAPE_HEIGHT = self.SHAPE_WIDTH #矩阵的
        self.currentShape = shape
        self.pos=[1,1] #random.randint(0,12)] #shape参考点在board上的位置
        self.lastPos = self.pos
        self.isDead = False #是否已‘死’，不能移动
        
 
    def rotate(self):
        '''
            旋转
        '''
        tmpshape=[]
        length =len(self.currentShape)
        tmpshape=[[x*0 for x in range(length)] for x  in range(length)]
        
        for x1 in range(length):
            for y1 in range(length):
                x2 = length-y1-1
                y2 = x1
                tmpshape[x2][y2] = self.currentShape[x1][y1]
        self.currentShape = tuple(tmpshape)

    def getCurrentShape(self):
        '''
            取得当前shape
        '''
        return self.currentShape
 
    def isDead(self):
        # 是否已经不能再下降了
        return self.isDead

    def setDead(self,state):
        self.isDead=state
 
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
        x = len(self.currentShape)
        print '\n'
        for i in range(x):
            print self.currentShape[i]


class Board():
    
    def __init__(self,movingShape,nextShape):
        self.WIDTH=12
        self.HEIGHT = 20
        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.movingShape = movingShape #正在下落的shape
        self.nextShape = nextShape

    #def modifyBody(self):
        

    def moveShapeToRight(self):

        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]


        '''
            将movingShape移动
        '''
        length = len(self.movingShape.getCurrentShape())
        if length ==3:
            position = self.movingShape.pos
            px = position[0]
            py = position[1]

            shape = self.movingShape.getCurrentShape()
            
            if (px+1)>self.WIDTH-2:#不能超出右边界
                return
            
            for x in range(px-1,px+2):
                for y in range(py-1,py+2):
                    if self.body[x+1][y] == 1 and shape[x-px][y-py] == 1:
                        return

            #如果不重叠，则移动
            position[1] += 1             
            
    def draw(self):
        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        
        #draw movingShape
        position = self.movingShape.pos
        px = position[0]
        py = position[1]

        shape = self.movingShape.getCurrentShape()

        #对应位置draw shape
        for x in range(px-1,px+2):
            for y in range(py-1,py+2):
                if shape[x-px][y-py] == 1:
                    self.body[x][y] = 1  

        for i in range(len(self.body)):
            print self.body[i]

    def getBody(self):
        return self.body

    def clearBoard(self):
        pass
        #self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]

    def appendShape(self,shape):
        self.moveShape=shape

    def update(self):
        x = self.movingShape.pos[0]
        y = self.movingShape.pos[1]
        


def spawnShape():
    global SHAPES
    return SHAPES[1]#random.randint(0, 6)]

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
print s2 

b = Board(s1,s2)
b.draw()
print '-------------------------'
b.moveShapeToRight()
b.draw()
