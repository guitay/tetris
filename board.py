# -*- coding: cp936 -*-

from string import lower
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

class Board(object):
    def __init__(self,movingShape,nextShape):
        self.WIDTH=12
        self.HEIGHT = 20
        self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.movingShape = movingShape #正在下落的shape
        self.nextShape = nextShape

    def moveLR(self,direction):

        '''
            将movingShape移动
        '''
        direct=-1
        if lower(direction) =='r' :#向左，向右
            direct = 1

        #self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]

        length = len(self.movingShape.getCurrentShape())
        if length ==3:
            position = self.movingShape.pos
            px = position[0]
            py = position[1]

            shape = self.movingShape.getCurrentShape()

            if (py-1)<0 or (py+1)>self.WIDTH-2:#不能超出左(右)边界
                print 'you cann''t move the shape out of the border. '
                return
                        
            for x in range(px-1,px+2):
                for y in range(py-1,py+2):
                    rp = relationPos((x,y+direct),(px,py+direct))
                    if self.body[x][y+direct] == 1 and shape[rp[0]][rp[1]] == 1:
                        return

            #如果不重叠，则移动
            position[1] = position[1]+direct            

    def moveDown(self):
        '''
            将shape下落
        '''
        #self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]

        length = len(self.movingShape.getCurrentShape())
        if length ==3:
            position = self.movingShape.pos #shape的参考点位置
            px = position[0]
            py = position[1]

            shape = self.movingShape.getCurrentShape()

            at_bottom = False      #是否到底      
            if (px+1)>self.HEIGHT-2:#不能超出底部边界
                print 'you cann''t move the shape out of the border. '
                at_bottom = True
            else:
                for x in range(px-1,px+2):
                    for y in range(py-1,py+2):
                        rp = relationPos((x+1,y),(px+1,py))
                        if (self.body[x+1][y] == 1 and shape[rp[0]][rp[1]] == 1) : 
                            at_bottom = True
                            break

            #如果不重叠，则移动
            if not at_bottom:
                position[0] += 1
            else:#modify board数组值，标识shape最终位置
                for x in range(px-1,px+2):
                    for y in range(py-1,py+2):
                        rp = relationPos((x,y),position)
                        if shape[rp[0]][rp[1]] == 1:
                            self.body[x][y] = 1

    def rotate(self):
        self.movingShape.rotate(self.body)

   
    def draw(self):
        print 'in board.draw():'
        #self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        
        #draw movingShape
        position = self.movingShape.pos
        px = position[0]
        py = position[1]

        shape = self.movingShape.getCurrentShape()

        print 'position:',position
        print 'self.movingShape.getCurrentShape()--->'
        print shape

        print '---------'

        #对应位置draw shape
        for x in range(px-1,px+2):
            for y in range(py-1,py+2):
                rp = relationPos((x,y),position)
                if shape[rp[0]][rp[1]] == 1:
                    self.body[x][y] = 1  

        for i in range(len(self.body)):
            print self.body[i]

    def getBody(self):
        return self.body

    def clearBoard(self):
        pass
        #self.body = [[x*0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]

    def appendShape(self,shape):
        self.movingShape=shape

    def update(self):
        x = self.movingShape.pos[0]
        y = self.movingShape.pos[1]


