#imports
import random
import sys
import time

import pygame
from pygame.locals import *

#initialzing
pygame.init()

#setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#other variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0

#setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load(r"C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\img\AnimatedStreet.png")
#create a white screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\img\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\img\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\img\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_HEIGHT-40),0)
    def move(self):
        global COIN
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_HEIGHT-40),0)
        elif Collide():
            COIN += 1
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, SCREEN_HEIGHT-self.rect.width),0)

#setting up sprites 
P1 = Player()
E1 = Enemy()
C1 = Coin()

#creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#add collide
def Collide():
    if pygame.sprite.spritecollideany(P1,coins):
        return True
    else:return False

#adding background music
pygame.mixer.music.load(r'C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\background.wav')
pygame.mixer.music.play(-1)

#adding a new user event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#game loop
while True:  

    #cycles through all events occurring 
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    money = font_small.render(str(COIN),True,RED)
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(money,(350,10))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    #moves and re-draws all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    #collision occurs between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis8\racer\crash.wav').play()
        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)