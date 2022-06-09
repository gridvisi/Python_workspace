
import pygame
pygame.init()
screen = pygame.display.set_mode([1040,640])
pygame.display.set_caption('bouncing ball')
screen.fill('light blue')
#pygame窗口框架程序
img = pygame.image.load("ballsmall.png")
x = 0  # x方向起始点
y = 0
speed = 5  #运动速度
running = True
while running:
    for event in pygame.event.get():
        if event.type-pygame.QUIT:
            running = False
    screen.blit(img,[x,y])
    pygame.display.update()
    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255],[x,y,100,100],0)
    #重绘矩形覆盖
    x += speed
    y += speed
    if x > 1040 or x <= 0:#碰到边缘反弹
        speed = -speed

    if y > 540 or y <= 0:#碰到边缘反弹
        speed = -speed

pygame.quit()



#任务二:参考程序 创客童年机器人
screen = pygame.display.set_mode([1040,720])
pygame.display.set_caption('bouncing ball')
screen.fill('light blue')
x = 270
y = 190
img = pygame.image.load("ballsmall.png")
speed_x = 6  #x轴方向上的速度
speed_y = 3  #y轴方向上的速度
running = True

while running:
    screen = pygame.display.set_mode([1040, 720])
    screen.fill('light gray')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit (img, [x,y])
    pygame.display.update()
    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255], [x,y,100,100],0)
    x += speed_x
    y += speed_y
    if x > 1040 or x <= 0:
        speed_x = -speed_x
    if y > 720 or y <= 0:
        speed_y = -speed_y
pygame.quit()


#pygame.display.flip()
#刷新屏幕重新画

