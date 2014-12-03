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
