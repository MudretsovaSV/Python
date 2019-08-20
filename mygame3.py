import pygame
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,255,0],[100,200],30,0)
pygame.draw.rect(screen,[20,50,10],[255,150,300,200],0)
pygame.draw.rect(screen,[20,50,10],[155,250,100,10],0)
pygame.draw.circle(screen,[0,0,0],[310,350],30,0)
pygame.draw.circle(screen,[0,0,0],[500,350],30,0)
pygame.draw.circle(screen,[250,250,0],[60,300],30,0)
pygame.draw.rect(screen,[55,150,160],[55,200,190,150],0)
pygame.draw.rect(screen,[255,255,255],[55,170,80,100],0)
pygame.draw.circle(screen,[0,0,0],[150,350],30,0)
pygame.draw.rect(screen,[5,5,160],[5,5,630,470],4)
pygame.draw.rect(screen,[255,5,160],[10,10,620,460],3)
pygame.draw.rect(screen,[250,255,0],[15,15,610,450],3)
pygame.draw.rect(screen,[0,255,0],[20,20,600,440],2)
#pygame.draw.circle(screen,[50,250,0],[60,300],30,0)
#my_list=[255,300,300,200]
#pygame.draw.rect(screen,[0,0,250],my_list,0)
#my_rect=pygame.Rect(250,150,300,200)
#pygame.draw.rect(screen,[0,255,0],my_rect,0)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()
