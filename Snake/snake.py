import pygame,random
from pygame.locals import *

def on_grid_random():
    x=random.randrange(0, 590, 10)
    y=random.randrange(0,590, 10)
    return (x, y)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_kin = pygame.Surface((10,10))
snake_kin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

score = 0

while True:
    
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

    
    if colisao(snake[0],apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score += 1
    
    
    print(snake[-1])

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if my_direction == UP:    
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    tela.fill((0,0,0))
    tela.blit(apple, apple_pos)

    for pos in snake:
        tela.blit(snake_kin, pos)

    pygame.display.update()
