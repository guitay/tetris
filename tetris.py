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
    W = 12          # board���������ٸ�����
    H = 20          # ������ٸ�����
    TILEW = 20      # ÿ�����ӵĸ�/���������
    START = (100, 20) # board����Ļ�ϵ�λ��
    SPACE = 1000    # �����ڶ��ٺ����ڻ�����(������level 1)
 
    def __init__(self, screen):
        self.stat = "game"
        self.WIDTH = self.TILEW * self.W
        self.HEIGHT = self.TILEW * self.H
        self.screen = screen
        # board���飬����ΪNone
        self.board = []
        for i in xrange(self.H):
            line = [ None ] * self.W
            self.board.append(line)
        # һЩ��Ҫ��ʾ����Ϣ
        self.level = 1
        self.killed = 0
        self.score = 0
        # ���ٺ��������£���Ȼ��init��϶��ǲ����(level����һ��
        self.time = self.SPACE * 0.8 ** (self.level - 1)
        # ��������Դ���һ�����º�����ʱ��
        self.elapsed = 0
        # used for judge pressed firstly or for a  long time
        self.pressing = 0
        # ��ǰ��shape
        self.shape = Shape(self.START,
                (self.WIDTH, self.HEIGHT), (self.W, self.H))
        # shape��Ҫ֪����Χ���������
        self.shape.set_board(self.board)
        # ����ǡ����硱�ġ����ա�
        self.board_image = pygame.Surface((self.WIDTH, self.HEIGHT))
        # ��һЩ��ʼ���Ļ���
        self.screen.blit(pygame.image.load(
            util.file_path("background.jpg")).convert(), (0, 0))
        self.display_info()

 
    def update(self, elapse):
        # ����Ϸ�׶Σ�ÿ�ζ����������������������룬���»���
        pass
 
    def move(self, u, d, l, r):
        # ���Ƶ�ǰ�����״̬
        pass
 
    def check_line(self):
        # �ж��Ѿ����·����״̬��Ȼ�����kill_line
        pass
 
    def kill_line(self, filled=[]):
        # ɾ���������У���Ҫ���Ÿ���������
        pass
 
    def get_score(self, num):
        # ����÷�
       pass
 
    def add_to_board(self):
        # �����׵ķ�����뵽board������
       pass
 
    def create_board_image(self):
        # �����һ���ȶ������ͼ��
        pass
 
    def next(self):
        # ������һ������
        pass
 
    def draw(self):
        # �ѵ�ǰ״̬������
        pass
 
    def display_info(self):
        # ��ʾ������Ϣ���������ȼ��ȣ������������_display***
        pass
 
    def _display_score(self):
        pass
 
    def _display_next(self):
        pass
 
    def game_over(self):
        # ��Ϸ����
        pass

class Shape():
    COLORS = ((0xcc, 0x66, 0x66), # ����shape����ɫ
        )

    def __init__(self,shape):
        self.SHAPE_WIDTH = len(shape) #����Ŀ��
        self.SHAPE_HEIGHT = self.SHAPE_WIDTH #�����
        self.currentShape = shape
        self.pos=[1,1] #random.randint(0,12)] #shape�ο�����board�ϵ�λ��
        self.lastPos = self.pos
        self.isDead = False #�Ƿ��ѡ������������ƶ�
        
 
    def rotate(self):
        '''
            ��ת
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
            ȡ�õ�ǰshape
        '''
        return self.currentShape
 
    def isDead(self):
        # �Ƿ��Ѿ��������½���
        return self.isDead

    def setDead(self,state):
        self.isDead=state
 
    def draw_current_shape(self):
        # ���Ƶ�ǰshhape��ͼ��
        pass
    def draw_next_shape(self):
        # ������һ��shape��ͼ��
        pass
    def _draw_shape(self, surface, shape, color):
        # ������������֧Ԯ����
        # ע������Ļ����ǻ��Ƶ�һ��surface�з��������draw����blit
        # �����ǻ�����Ļ��
        pass
 
    def draw(self, screen):
        # ����shape����Ļ��
        x = len(self.currentShape)
        print '\n'
        for i in range(x):
            print self.currentShape[i]


class Board():
    
    def __init__(self,movingShape,nextShape):
        self.WIDTH=12
        self.HEIGHT = 20
        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.movingShape = movingShape #���������shape
        self.nextShape = nextShape

    #def modifyBody(self):
        

    def moveShapeToRight(self):

        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]


        '''
            ��movingShape�ƶ�
        '''
        length = len(self.movingShape.getCurrentShape())
        if length ==3:
            position = self.movingShape.pos
            px = position[0]
            py = position[1]

            shape = self.movingShape.getCurrentShape()
            
            if (px+1)>self.WIDTH-2:#���ܳ����ұ߽�
                return
            
            for x in range(px-1,px+2):
                for y in range(py-1,py+2):
                    if self.body[x+1][y] == 1 and shape[x-px][y-py] == 1:
                        return

            #������ص������ƶ�
            position[1] += 1             
            
    def draw(self):
        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        
        #draw movingShape
        position = self.movingShape.pos
        px = position[0]
        py = position[1]

        shape = self.movingShape.getCurrentShape()

        #��Ӧλ��draw shape
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
