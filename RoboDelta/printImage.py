import pygame
from pygame.locals import *

LARGURA=600
ALTURA=600
    
pygame.init()
screen = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Pac Man')

x=[]
y=[]
cor=[]


image = pygame.image.load('logo.txt')


while True:
    screen.blit(image, (0,0))    
    pygame.display.update()
