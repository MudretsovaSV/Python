import pygame, sys, random
skier_images=["skier_down.png", "skier_right1.png",
              "skier_right2.png", "skier_left2.png",
              "skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("skier_down.png")
        self.rect=self.image.get_rect()
        self.rect.center=[320,100]
        self.angel=0
# создаем лыжника

    def turn(self,direction):
        self.angel=self.angel+direction
        if self.angel<-2: self.angel=-2
        if self.angel>2: self.angel=2
        center=self.rect.center
        self.image=pygame.image.load(skier_images[self.angel])
        self.rect=self.image.get_rect()
        self.rect.center=center
        speed=[self.angel,6-abs(self.angel)*2]
        return speed
# поворачиваем лыжника

    def move(self,speed):
        self.rect.centerx=self.rect.centerx+speed[0]
        if self.rect.centerx<20: self.rect.centerx=20
        if self.rect.centerx>620: self.rect.centerx=620
# двигаем лыжника влево и вправо

class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file=image_file
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.center=location
        self.type=type
        self.passed=False
# создаем деревья и флаги

    def update(self):
        global speed
        self.rect.centery -=speed[1]
# обеспечиваем прокрутку игрового фона
        if self.rect.centery<-32:
            self.kill()
# удаляем препятствия, ушедшие за верхнюю границу экрана

def create_map():
    global obstacles
    locations=[]
    for i in range(10):
        row=random.randinit(0,9)
        col=random.randinit(0,9)
        location=[col*64+32, row*64+32+640]
        if not (location in locations):
            locations.append(location)
            type=random.choice(["tree", "flag"])
            if type=="tree": img="skier_tree.png"
            elif type=="flag": img="skier_flag.png"
            obstacle=ObstacleClass(img,location,type)
            obstacles.add(obstacle)
# создаем экран со случайным образом расположенными деревьями и флагами

def animate():
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(scier.image,skier.rect)
    screen.blit(score_text,[10,10])
    pygame.display.flip()
# обновляем экран

pygame.init()
screen=pygame.display.set_mode([640,640])
clock=pygame.time.Clock()
skier=SkierClass()
speed=[0,6]
obstacles=pygame.sprite.Group()
map_position=0
points=0
create_map()
font=pygame.font.Font(None,50)
# готовим все к запуску

running=True
while running: # запускаем основной цикл
    clock.tik(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if evet.key==pygame.K_LEFT:
                speed=skier.turn(-1)
            elif event.key==pygame.K_RIGHT:
                speed=skier.turn(1)
# проверяем нажатие клавиш или закрытие окна
skier.move(speed)
# перпемещаем лыжника
map_position += speed[1] # прокручиваем экран

if map_position>=640:
    create_map()
    map_position=0

hit =  pygame.sprite.spritecollide(skier, obstacles, False)
if hit:
        if hit[0].type == "tree" and not hit[0].passed:  #crashed into tree  
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")  # crash image
            animate()  
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")  # resume skiing
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:   # got a flag
            points += 10
            hit[0].kill()                                 # remove the flag 
    
    obstacles.update()
    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
    animate()
pygame.quit()
