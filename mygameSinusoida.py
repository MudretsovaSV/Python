import pygame, sys
import math

pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for x in range(0,640):
    y=int(math.sin(x/640.0*15*math.pi)*100+240)
   # pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
    screen.set_at([x,y],[0,0,200])
    pixel_color=screen.get_at([320,240])
    
plotPoints=[]
for x in range(0,640):
    y=int(math.sin(x/640.0*4*math.pi)*200+240)
    plotPoints.append([x,y])
pygame.draw.lines(screen,[255,0,0],False,plotPoints,3

dots=[[221,432],[225,331],[133,342],[141,310],
      [51,230],[74,217],[58,153],[114,164],
      [123,135],[176,190],[159,77],[193,93],
      [230,28],[267,93],[301,77],[284,190],
      [327,135],[336,164],[402,153],[386,217],
      [409,230],[319,310],[327,342],[233,331],
      [237,432]]
pygame.draw.lines(screen,[20,200,20],True,dots,2)

pygame.draw.polygon(screen, [0,200,250], [[500,200],[400,250],[400,300],[600,300],[600,250]], 6)
pygame.draw.ellipse(screen, [100,20,250], [[350,50],[100,150]], 6)
pygame.draw.line(screen, [100,120,50], [350,50],[100,150], 6)
pygame.draw.lines(screen,[0,50,0], False, [[0, 80], [50, 90], [200, 80], [220, 30],[300,25]], 5)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()
#------------------------------------------------------------------



