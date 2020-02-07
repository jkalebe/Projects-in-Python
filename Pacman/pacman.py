import pygame, random
from pygame.locals import *
from pygame import image, Color
from random import choice

UP=1
DOWN=2
LEFT=3
RIGHT=4

LARGURA=600
ALTURA=600
    
pygame.init()
screen = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Pac Man')

pacman = image.load('player.png')
pacman = pygame.transform.scale(pacman, (20,20))
pacman_pos = (20,20)

monstro = image.load('ghost1.png')
monstro = pygame.transform.scale(monstro, (20,20))
monstro_pos=((300,280))

dotimage = image.load('pacmandotmap.png')

pacmanmovemap = image.load('pacmanmovemap.png')


colourmap = image.load('colourmap.png')


pacman_right = pacman
pacman_left = pygame.transform.rotate(pacman, -180)
pacman_up = pygame.transform.rotate(pacman, 90)
pacman_down = pygame.transform.rotate(pacman, -90)


apple = pygame.Surface((5,5))
apple.fill((255,0,0))
apple_pos = []
for i in range (5, LARGURA,20):
    for j in range (5, ALTURA-20,20):
        if dotimage.get_at((i,j)) == Color('black'):
            apple_pos.append((i, j))

def isColisao(pos_pacman, pos_monstro):
    if pos_pacman[0]==pos_monstro[0] and pacman_pos[1] == pos_monstro[1]:
        return True

my_direction=LEFT

def moveMonstro(pos):
    if pos[0]-20 < 0:
        pos[0] = pos[0]+600
    if pos[0]+20 >600:
        pos[0] = pos[0]-600

    possibles=[]
    if pos[0]+20 < 600:
        if pacmanmovemap.get_at((pos[0]+20, pos[1])) == Color('black'):
            possibles.append('right')
    if pos[0]-20 > 0:
        if pacmanmovemap.get_at((pos[0]-20, pos[1])) == Color('black'):
            possibles.append('left')
    if pos[1]+20 < 580:
        if pacmanmovemap.get_at((pos[0], pos[1]+20)) == Color('black'):
            possibles.append('down')
    if pos[1]-20 < 580:
        if pacmanmovemap.get_at((pos[0], pos[1]-20)) == Color('black'):
            possibles.append('up')

    direction = choice(possibles)

    if direction == 'up':
        new_pos = (pos[0], pos[1]-20)
    if direction == 'down':
        new_pos = (pos[0], pos[1]+20)
    if direction == 'left':
        new_pos = (pos[0]-20, pos[1])
    if direction == 'right':
        new_pos = (pos[0]+20, pos[1])

    return new_pos

gameOver=False
while not gameOver:
    
    my_direction = -1
    
    if pygame.time.get_ticks() % 10 == 0:
        monstro_pos = moveMonstro(pos=monstro_pos)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            
            if event.key == K_UP and pacman_pos[1] > 0 :
                my_direction=UP
            
            if event.key == K_DOWN and pacman_pos[1] < (ALTURA-20):
                my_direction=DOWN
                
            if event.key == K_RIGHT and pacman_pos[0] < (LARGURA-20):
                my_direction=RIGHT
                
            if event.key == K_LEFT and pacman_pos[0] > 0:
                my_direction=LEFT
                
    
    if my_direction == UP:
        pacman_pos = (pacman_pos[0], pacman_pos[1]-20)
        pacman = pacman_up
        if pacmanmovemap.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0], pacman_pos[1]+20)
    if my_direction == DOWN:
        pacman_pos = (pacman_pos[0], pacman_pos[1]+20)
        pacman = pacman_down
        if pacmanmovemap.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0], pacman_pos[1]-20)
    if my_direction == RIGHT:
        pacman_pos = (pacman_pos[0]+20, pacman_pos[1])
        pacman = pacman_right
        if pacmanmovemap.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0]-20, pacman_pos[1])
    if my_direction == LEFT:
        pacman_pos = (pacman_pos[0]-20, pacman_pos[1])
        pacman = pacman_left
        if pacmanmovemap.get_at(pacman_pos) == Color('white'):
            pacman_pos = (pacman_pos[0]+20, pacman_pos[1])
    
    gameOver = isColisao(pacman_pos, monstro_pos)

    collision = -1
    for i in range(len(apple_pos)):
        if pacman.get_rect(center=(pacman_pos[0]+10, pacman_pos[1]+10)).collidepoint(apple_pos[i][0], apple_pos[i][1]):
            collision = i
    if collision != -1:
        apple_pos.pop(collision)

    screen.blit(colourmap, (0,0))
    
    for pos in apple_pos:
        screen.blit(apple, pos)

    screen.blit(pacman, pacman_pos)
    
    
    screen.blit(monstro, monstro_pos)
    
    pygame.display.update()