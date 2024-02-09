from random import randint,choice
import keyboard
import pygame
from sys import exit

class Snake:
    def __init__(self):
        self.headx=(randint(0,(1920//20))*20)
        self.heady=(randint(40//20,(1040//20)//2)*20)
        self.direction=choice([(0,1),(0,-1),(1,0),(-1,0)])#use choice to make it random
        self.length=20
        self.pieces=[]
class Apple():
    def __init__(self):
        self.applex=(randint(0,1900//20)*20)
        self.appley=(randint(0,1020//20)*20)
        self.exist=False
    def reset(self):
        self.applex = (randint(0, 1900//20)*20)
        self.appley = (randint(0, 1020//20)*20)


snake = Snake()
apple = Apple()

appleimg = pygame.image.load('apple.bmp')

def handle_key_event(key):
    if key.event_type == keyboard.KEY_DOWN and key.name in ['w','a','s','d']:
        globals()[key.name]()
    else:pass

def w():snake.direction=(0,-1)
def s():snake.direction=(0,1)
def a():snake.direction=(-1,0)
def d():snake.direction=(1,0)
keyboard.hook(handle_key_event)#fix keyboard input don't care if it looks ugly



pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()

while 1:
    screen.fill((0,0,0))
    if apple.exist==False:screen.blit(appleimg,(apple.applex,apple.appley))

    snake.pieces.append((
        snake.headx,
        snake.heady))

    snake.pieces=snake.pieces[-snake.length//10:]
    snake.headx=((snake.headx+snake.direction[0]*20)%1920)
    snake.heady=((snake.heady+snake.direction[1]*20)%1040)

    for x in range(len(snake.pieces)):pygame.draw.rect(screen,(0,255,0),(snake.pieces[x][0],snake.pieces[x][1],18,18))

    if (snake.headx,snake.heady) in snake.pieces:
        snake=Snake()
        apple.reset()
    if (snake.headx,snake.heady) == (apple.applex,apple.appley):
        snake.length+=10
        apple.reset()

    pygame.draw.rect(screen, (0, 255, 0), (snake.headx, snake.heady, 18, 18))
    pygame.display.flip()
    clock.tick(30)
