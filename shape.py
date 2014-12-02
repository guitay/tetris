# -*- coding: cp936 -*-
#from tetris import relationPos



def relationPos(p1,pos):
    x=p1[0]
    y = p1[1]
    px = pos[0]
    py = pos[1]
    if x == px-1:
        x1=0
    elif x==px+1:
        x1=2
    else:
        x1=x
    if y == py-1:
        y1=0
    elif y==py+1:
        y1=2
    else:
        y1=y

    return (x1,y1)

class Shape(object):
    COLORS = ((0xcc, 0x66, 0x66), # ����shape����ɫ
        )

    def __init__(self,shape):
        self.SHAPE_WIDTH = len(shape) #����Ŀ��
        self.SHAPE_HEIGHT = self.SHAPE_WIDTH #�����
        self.currentShape = shape
        self.pos=[1,1] #random.randint(0,12)] #shape�ο�����board�ϵ�λ��
        self.lastPos = self.pos
        self.isDead = False #�Ƿ��ѡ������������ƶ�

    def check_rotate(self,rotated_shape,body):
        print
        print 'body--->'
        print body
        print 
        length = len(rotated_shape)
        
        canRotated = True      #�Ƿ����ת
        if length ==3:
            position = self.pos #shape�Ĳο���λ��
            px = position[0]
            py = position[1]
    
            for x in range(px-1,px+2):
                for y in range(py-1,py+2):                    
                    rp = relationPos((x,y),(px,py))
                    if (body[x][y] == 1 and rotated_shape[rp[0]][rp[1]] == 1) : 
                        canRotated = False
                        break
                    
        return canRotated        
 
    def rotate(self,body):
        '''
            ��ת
        '''
        tmpshape=[]
        length =len(self.currentShape)
        tmpshape=[[x*0 for x in range(length)] for x  in range(length)]

        print 'self.currentShape--->'
        print self.currentShape

        print 
        
        for x1 in range(length):
            for y1 in range(length):
                x2 = length-y1-1
                y2 = x1
                tmpshape[x2][y2] = self.currentShape[x1][y1]
        rotated_Shape = tuple(tmpshape)

        print 'rotated_shape-->'
        print rotated_Shape
        
        if self.check_rotate(rotated_Shape,body):
            print 'modify currentShape.....'
            self.currentShape = rotated_Shape


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

