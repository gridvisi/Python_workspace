import math
import turtle
import pygame
# 红旗长宽比为3: 2
num_times = 50
width, height = 30 * num_times, 20 * num_times
# 初始化屏幕和海龟对象
screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(1)

t.penup()
t.goto(-width/2, height/2)
t.pendown()
t.begin_fill()
t.fillcolor('red')
t.fd(width)
t.right(90)
t.fd(height)
t.right(90)
t.fd(width)
t.right(90)
t.fd(height)
t.right(90)
t.end_fill()

'''画多边形'''
def drawPolygon(t, side_len, num_angles=5, color=None):
  if color is not None:
    t.begin_fill()
    t.fillcolor(color)
  for i in range(num_angles):
    t.forward(side_len)
    t.left(360 / num_angles)
    t.forward(side_len)
    t.right(720 / num_angles)
  if color is not None:
    t.end_fill()

'''画5角星'''
def draw5AnglesStar(t, start_pos, end_pos, radius, color=None):
    side_len = radius * math.sin(math.pi/5) / math.sin(math.pi*2/5)
    t.left(math.degrees(math.atan2(end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    t.penup()
    t.goto(start_pos)
    t.fd(radius)
    t.pendown()
    t.right(math.degrees(math.pi * 9 / 10))
    drawPolygon(t, side_len, 5, color)


draw5AnglesStar(t, start_pos=(-10*num_times, 5*num_times), end_pos=(-10*num_times, 8*num_times), radius=3*num_times, color='yellow')
for pos in [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]:
  draw5AnglesStar(t, start_pos=(pos[0]*num_times, pos[1]*num_times), end_pos=(-10*num_times, 5*num_times), radius=1*num_times, color='yellow')
#最后，再加上国歌作为背景音乐：
'''播放背景音乐'''
def playBGM(bgm_path):
  pygame.mixer.init()
  bgm = pygame.mixer.music.load(bgm_path)
  pygame.mixer.music.play(-1)