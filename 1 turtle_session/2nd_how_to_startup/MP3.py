import time
import pygame

def play_music(self):
    filepath = r"E:\music\消愁.mp3"
    pygame.mixer.init()
    # 加载音乐
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(start=0.0)
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    time.sleep(300)
    pygame.mixer.music.stop()

play_music(self)
'''
from Tkinter import *
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('sound.wav')
snd.play(blocking=1)
'''


'''
import os
file = 'test.mp3'
os.system('mpg123’+ file')
from playsound import playsound
playsound('test.mp3')
'''