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
    # shape�ǻ���һ�����������
    # ��Ϊ�����в�ͬ��ģʽ�����Ծ������ϢҲҪ��ϸ����
    SHAPEW = 4    # ����Ǿ���Ŀ��
    SHAPEH = 4    # ����Ǹ߶�
    SHAPES = ()
    COLORS = ((0xcc, 0x66, 0x66), # ����shape����ɫ
        )
 
    def __init__(self, board_start, (board_width, board_height), (w, h)):
        self.start = board_start
        self.W, self.H = w, h           # board�ĺᡢ�ݵ�tile��
        self.length = board_width / w   # һ��tille�ĳ���(������)
        self.x, self.y = 0, 0     # shape����ʼλ��
        self.index = 0          # ��ǰshape��SHAPES�ڵ�����
        self.indexN = 0         # ��һ��shape��SHAPES�ڵ�����
        self.subindex = 0       # shape����������һ������
        self.shapes = []        # ��¼��ǰshape���ܵĳ���
        self.color = ()
        self.shape = None
        # ������Surface������ŵ�ǰ����һ��shape��ͼ��
        self.image = pygame.Surface(
                (self.length * self.SHAPEW, self.length * self.SHAPEH),
                SRCALPHA, 32)
        self.image_next = pygame.Surface(
                (self.length * self.SHAPEW, self.length * self.SHAPEH),
                SRCALPHA, 32)
        self.board = []         # �����Ϣ
        self.new()            # let's dance!
 
    def set_board(self, board):
        # �������״��������
        pass
 
    def new(self):
        # �²���һ������
        # ע��������ʵ���²�������һ�������飬������Ҫ���µķ�����
        # ����һ������һ��������������
        pass
 
    def rotate(self):
        # ��ת
        pass
 
    def move(self, r, c):
        # �����·�����ƶ�
        pass
 
    def check_legal(self, r=0, c=0):
        # ���������move�ж��У����������ƶ����Ƿ�Ϸ������Ƿ�Խ�磩
        # �Ϸ��Ż�ʵ�ʵĶ���
        pass
 
    def at_bottom(self):
        # �Ƿ��Ѿ��������½���
        pass
 
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
