import numpy
import pygame
pygame.init()
WIDTH,HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

def computeMandelbrot(nMax,accuracy,xR,yR):
    x = numpy.linspace(xR[0],xR[1],WIDTH)
    y = numpy.linspace(yR[0],yR[1],HEIGHT)
    pList = []
    for i_x in x:
        pList.append([])
    for i_x in range(len(x)):
        for i_y in y:
            pList[i_x].append(0)
    intX = 0
    for i_x in x:
        intY = 0
        for i_y in y:
            c = i_x + 1j*i_y
            z = c
            iter = 0
            try:
                for i in range(nMax):
                    iter += 1
                    z = z**2+c
                    if abs(z)>4:
                        break
                if abs(z)>accuracy:
                    pList[intX][(HEIGHT-intY)-1] = (iter/nMax*255,0,0)
                else:
                    pList[intX][(HEIGHT-intY)-1] = (0,0,0)
            except OverflowError:
                continue
            intY+=1
        intX +=1
    return pList
rangeX = (-2,1.5)
rangeY = (-2,2)
run = True
pList = []
def updatePList(rangeX,rangeY):
    global pList
    pList = computeMandelbrot(150,4,rangeX,rangeY)
def updateMandel():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            WIN.set_at((x,y),pList[x][y])
updatePList(rangeX,rangeY)
p1 = ()
p2 = ()
holding = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            p1 = pygame.mouse.get_pos()
            holding = True
        elif event.type == pygame.MOUSEBUTTONUP:
            p2 = pygame.mouse.get_pos()
            holding = False
            rangeX1 = (rangeX[1]-rangeX[0])*(p1[0]/WIDTH)+rangeX[0]
            rangeX2 = (rangeX[1]-rangeX[0])*(p2[0]/WIDTH)+rangeX[0]
            rangeY1 = (rangeY[0]-rangeY[1])*(p1[1]/HEIGHT)+rangeY[1]
            rangeY2 = (rangeY[0]-rangeY[1])*(p2[1]/HEIGHT)+rangeY[1]
            if rangeX1<rangeX2:
                rangeX = (rangeX1,rangeX2)
            else:
                rangeX = (rangeX2,rangeX1)
            if rangeY1<rangeY2:
                rangeY = (rangeY1,rangeY2)
            else:
                rangeY = (rangeY2,rangeY1)
            updatePList(rangeX,rangeY)
    WIN.fill((0,0,0))
    updateMandel()
    if holding:
        p2 = pygame.mouse.get_pos()
        pygame.draw.lines(WIN,(0,0,255),True,[p1,(p1[0],p2[1]),p2,(p2[0],p1[1])],1)
    pygame.display.update()
