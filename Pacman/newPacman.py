import pygame, random
from pygame.locals import *
from pygame import image, Color
from random import choice

UP=0
DOWN=1
LEFT=2
RIGHT=3

pacman = image.load('player.png')
pacman = pygame.transform.scale(pacman, (20,20))
pacman_pos = (20,20)

monstro = image.load('ghost1.png')
monstro = pygame.transform.scale(monstro, (20, 20))
monstro_pos = (280,280)

pacman_move_map = image.load('pacmanmovemap.png')

map_comida_pacman = image.load('pacmandotmap.png')

colour_map = image.load('colourmap.png')

apple = pygame.Surface((5,5))
apple.fill((255,0,0))

apple_pos=[]
for i in range(5, 600, 20):
    for j in range(5, 580, 20):
        if map_comida_pacman.get_at((i,j)) == Color('black'):
            apple_pos.append((i,j))

def colisao(c1, c2):
    return (c1[0] == c2[0])and (c1[1] == c2[1])


pygame.init()
screen=pygame.display.set_mode((600,600)) #criar janela
pygame.display.set_caption('PacMan')



my_direcao=RIGHT

while True:
    my_direcao = -1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP :
                my_direcao = UP
            
            if event.key == K_DOWN:
                my_direcao = DOWN
            
            if event.key == K_RIGHT:
                my_direcao = RIGHT
            
            if event.key == K_LEFT:
                my_direcao = LEFT
            
    
    if my_direcao == UP:
        pacman_pos = (pacman_pos[0], pacman_pos[1] - 20)
        if pacman_move_map.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0], pacman_pos[1] + 20)

    if my_direcao == DOWN:
        pacman_pos = (pacman_pos[0], pacman_pos[1] + 20)
        if pacman_move_map.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0], pacman_pos[1] - 20)

    if my_direcao == RIGHT:
        pacman_pos = (pacman_pos[0] + 20, pacman_pos[1])
        if pacman_move_map.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0] - 20, pacman_pos[1])

    if my_direcao == LEFT:
        pacman_pos = (pacman_pos[0] - 20, pacman_pos[1])
        if pacman_move_map.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0] + 20, pacman_pos[1])

    collision = -1
    for i in range(len(apple_pos)):
        if pacman.get_rect(center=(pacman_pos[0]+10, pacman_pos[1]+10)).collidepoint(apple_pos[i][0], apple_pos[i][1]):
            collision = i
    if collision != -1:
        apple_pos.pop(collision)

    screen.blit(colour_map, (0,0))

    screen.blit(pacman, pacman_pos)
    for pos in apple_pos:
        screen.blit(apple, pos)
    
    pygame.display.update()