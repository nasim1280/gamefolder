import pygame
import random
import sys
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()

def step(event,xchange,ychange):
    step = 3
    
    if event.key == pygame.K_LEFT:
        xchange = -step
        ychange = 0
    elif event.key == pygame.K_RIGHT:
        xchange = step
        ychange = 0
    elif event.key == pygame.K_UP:
        xchange = 0
        ychange = -step
    elif event.key == pygame.K_DOWN:
        xchange = 0
        ychange = step
    return(xchange,ychange)

def move(x_player , y_player, xchange,ychange):
    x_player += xchange
    y_player += ychange
    x_player = x_player%880
    y_player = y_player%480
    return (x_player , y_player)

def collide(x_player,y_player,player_size,
         x_evil  ,y_evil  ,evil_size,
         x_heart ,y_heart ,heart_size):
    position_player = Rect([x_player, y_player, player_size, player_size])
    position_evil   = Rect([x_evil  , y_evil  , evil_size  , evil_size])
    position_heart  = Rect([x_heart , y_heart , heart_size , heart_size])
    collide_player_evil  = pygame.Rect.colliderect(position_player, position_evil)
    collide_player_heart = pygame.Rect.colliderect(position_player, position_heart)
    return (collide_player_evil , collide_player_heart)

def randoms():
    x_evil  = random.randrange(20,880,10)
    y_evil  = random.randrange(20,480,10)
    x_heart = random.randrange(20,880,10)
    y_heart = random.randrange(20,480,10)
    return (x_evil , y_evil , x_heart , y_heart) 
    
def hearts():
    heart_list = ["heart1.jfif" ,"heart2.jfif" , "heart3.jfif" , "heart4.jpg"] 
    heart_file = random.choice(heart_list)
    heart = pygame.image.load(heart_file)
    return heart

def evils():
    evil_list = ["evil1.jfif" ,"evil2.jfif" , "evil3.jfif"] 
    evil_file = random.choice(evil_list)
    evil = pygame.image.load(evil_file)
    return evil

def maps(screen):
    screen_color=(200,190,190)
    screen.fill(screen_color)
    background_level1 = pygame.image.load("background_level1.png")
    #background_level2 = pygame.image.load("background_level2.png")
    screen.blit(background_level1, [0,0])

def shows(x_player,y_player,player_size,
          x_evil  ,y_evil  ,evil_size,
          x_heart ,y_heart ,heart_size,
          player , heart , evil):
    player = pygame.transform.scale(player, [player_size, player_size])
    screen.blit(player, [x_player,y_player])
    heart = pygame.transform.scale(heart, [heart_size, heart_size])
    screen.blit(heart, [x_heart,y_heart])
    evil = pygame.transform.scale(evil, [evil_size, evil_size])
    screen.blit(evil, [x_evil,y_evil])
             
screen=pygame.display.set_mode((900,500))
pygame.display.set_caption('Eat hearts Not evils!')
Time = pygame.time.Clock()

player_size , heart_size , evil_size = 50 , 50 , 50
x_player , y_player = 400 , 200
x_evil , y_evil = 400 , 400
x_heart , y_heart = 50 , 200
xchange , ychange = 0 , 0

player = pygame.image.load("hearteyes.jfif")
heart = pygame.image.load("heart1.jfif")
evil = pygame.image.load("evil1.jfif")

mixer.music.load("music1.wav")
mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
        if event.type == pygame.KEYDOWN:
            xchange , ychange = step(event,xchange,ychange)

    x_player,y_player = move(x_player , y_player , xchange,ychange)

    collide_player_evil,collide_player_heart = collide(x_player,y_player,player_size,
                                                    x_evil  ,y_evil  ,evil_size,
                                                    x_heart ,y_heart ,heart_size)

    if collide_player_heart:
        x_evil , y_evil , x_heart , y_heart = randoms()
        player_size += 20
        heart = hearts()
        evil  =  evils()
    if collide_player_evil:
        
        break
        
    maps(screen)
    shows(x_player,y_player,player_size,
          x_evil  ,y_evil  ,evil_size,
          x_heart ,y_heart ,heart_size,
          player , heart , evil)
    
    pygame.display.update()
    Time.tick(75)
gameover = pygame.image.load("gameover.png")
screen.blit(gameover, [150,150])
pygame.display.update()

Time.tick(0.4)
pygame.quit()   

