import pygame,random
from random import randint
from pygame import mixer
from pygame import K_DOWN,KEYDOWN,K_LEFT,K_RIGHT,K_0
import time
import sys, os
file_dir = os.path.dirname("C://Users//90553//PycharmProjects//pythonProject//venv//Lib//site-packages//pygame")
sys.path.append(file_dir)
pygame.init()
ekran = pygame.display.set_mode([600,600])
run =True
top=pygame.image.load("top.png")
topx=randint(0,600)
topy=randint(0,600)
x=300
y=300
skor=0
yazı=pygame.font.SysFont("monospace",15)
label = yazı.render(("Skorunuz " + str(skor)), 3, (0,0,0))
yazıyeri=(500,50)
current=1
uzunlukx=5
uzunluky=50
art=0.03
currentup=1
while run:
    ekran.fill((255, 255, 255))
    ekran.blit(label,yazıyeri)
    ekran.blit(top,(topx,topy))
    if current==1:
        if currentup==1:
            y=y-art
        else:
            y=y+art
    else:
        if currentup==1:
            x=x+art
        else:
            x=x-art
    if (x+uzunlukx>600 or x-(skor*10)<0) or (y+uzunluky>600 or y-(skor*10)<0):
        label = yazı.render(("Skorunuz " + str(skor)+" Oyun bitti"), 3, (0,0,0))
        yazıyeri=(300,300)
        run=False
    if ((topx-(x+uzunlukx)<=20 and topx-x-uzunlukx>=0) or (x+uzunlukx-topx<=20 and x+uzunlukx-topx>=0)) and ((topy-y<=20 and topy-y>=0) or (y-topy<=20 and y-topy>=0)):
        skor=skor+1
        label = yazı.render(("Skorunuz " + str(skor)), 3, (0,0,0))
        topx=randint(0+(uzunlukx+skor*10),600-(uzunlukx+skor*10))
        topy=randint(0+(uzunluky+skor*10),600-(uzunluky+skor*10))
    i=0
    while i<=skor:
        if current==1:
            pygame.draw.line(ekran, (0,0,0), (x, y-(i*10)),(x+uzunlukx,y-(i*10)+uzunluky), 20)
        else:
            pygame.draw.line(ekran, (0,0,0), (x-(i*10), y),(x-(i*10)+uzunlukx,y+uzunluky), 20)
        i=i+1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.QUIT:
                run=False
            if event.key==K_LEFT:
                if currentup==1:
                    currentup=0
                if current==1:
                    current=0
                    hold=uzunluky
                    uzunluky=uzunlukx
                    uzunlukx=hold
                x=x-20
            if event.key==K_RIGHT:
                if currentup==0:
                    currentup=1
                if current==1:
                    current=0
                    hold=uzunluky
                    uzunluky=uzunlukx
                    uzunlukx=hold
                x=x+20
            if event.key==K_DOWN:
                if currentup==1:
                    currentup=0
                if current==0:
                    current=1
                    hold=uzunluky
                    uzunluky=uzunlukx
                    uzunlukx=hold
                y=y+20
            if event.key==pygame.K_UP:
                if currentup==0:
                    currentup=1
                if current==0:
                    current=1
                    hold=uzunluky
                    uzunluky=uzunlukx
                    uzunlukx=hold
                y=y-20
