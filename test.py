
shape1 = [[0,1,0,0],\
          [1,1,0,0],\
          [0,1,0,0],
          [0,0,0,0],]

#print shape1
#print type(shape)

#0,0 -> 3,0
#0,1 -> 2,0
#0,2 -> 1,0
#0,3 -> 0,0

#0,1 -> 1,0
#1,0 -> 2,1
#1,1 -> 1,1
#1,2 -> 0,1

#2,1 -> 1,2

def rotate():
    shape2=[[x*0 for x in range(4)] for x in range(4)]
    for x1 in range(4):
        for y1 in range(4):
            x2 = 4-y1-1
            y2 = x1
            shape2[x2][y2] = shape1[x1][y1]
    return shape2



def rotate2():
    shape2=[[0,0,0],[0,0,0],[0,0,0]]
    for x1 in range(3):
        for y1 in range(3):
            y2 = x1
            if y1==2 :
                x2=0
            elif y1==1:
                x2=1
            else:
                x2=2
            shape2[x2][y2] = shape1[x1][y1]
    return shape2

def printShape():
    print 
    for i in range(4):
        print shape1[i]
        
printShape()
shape1 = rotate()
printShape()
shape1 = rotate()
printShape()
shape1 = rotate()
printShape()
shape1 = rotate()
printShape()
