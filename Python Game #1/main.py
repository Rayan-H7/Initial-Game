import pygame
from random import randint
#Imports the pygame and random module
pygame.init()
#Generates a random number
rand_num = randint(1,255)
#Creates player character
player = pygame.Rect((rand_num,rand_num,rand_num,rand_num))
#Initialises the pygame to be created
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
#Sets the screen width and height
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Displays screen with correct dimensions
run = True
#This will keep the screen running constantly
while run:
    screen.fill((0,rand_num,0))
    #Epilepsy time!
    rand_num = randint(1,255)
    rand_num2 = randint(1,255)
    rand_num3 = randint(1,255)
    pygame.draw.rect(screen,(rand_num,rand_num2,rand_num3),player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0,1)
    elif key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

