import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption('car driven_thru')

#汽车动起来


#绘制马路左右边界
import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.line(screen,[0,0,0],[200,0],[80,480],5)
#绘制左边界 pygame.drawline(screen,[000][4400],[560480]5)
# #绘制右边界
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rurning = False
pygame. quit()



#绘制马路中间的虚线

def linemiddle():#画马路中间虚线
    plotpoints=[]
    x=320
    for y in range(0,500,20):
        plotpoints.append([x,y])
        if len(plotpoints)-2:
            pygame.drawlines(screen,[0,0,0],False,plotpoints,5)
            plotpoints=[]
            pygame.displayupdate()



my_car = pygame.image.load("car.ipeg")
y=340
linemiddle()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    screen.blit(my_car,[330,y])
    pygame.display.update()
    pygame.time.delay(200)
    pygame.draw.rect(screen,[255,255,255],[330,y,90,140],0)
    y -= 50
    if y <= -140:
        y= 340
pygame.quit()
