import pygame, sys

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('动画测试')
image = pygame.image.load(r'ballsmall.png')
rect = image.get_rect()
rect2 = pygame.Rect(0, 0, rect.width // 4, rect.height)
tick = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for n in range(4):
        tick.tick(4)
        rect2.x += n * rect2.width
        if rect2.x > 1000:
            rect2.x = 0
        screen.fill((255, 255, 255))
        screen.blit(image, (0, 0), rect2)
        # 这里给了3个实参,分别是图像,绘制的位置,绘制的截面框
        pygame.display.flip()