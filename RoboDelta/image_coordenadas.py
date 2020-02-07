import pygame
from pygame.locals import *
from pygame import image
import datetime



#pygame.init()
#screen = pygame.display.set_mode((600,600))
#image1 = image.load('images.png')
image1 = image.load('instagram_f_branco.png')
image1 = pygame.transform.scale(image1, (150,150))

#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.QUIT()
#            exit()
print(f'largura: {image1.get_size()[0]}')
print(f'altura: {image1.get_size()[1]}')
arquivo = open('logo.txt', 'w')



for i in range(image1.get_size()[0]):
    for j in range(image1.get_size()[1]):
        #print(f'x, y = {image1.get_at((i,j))}')
        #l_c= image1.get_at((i,j))
        cor = image1.get_at((i,j))
        z=0
        if cor != (255,255,255,255):
            cor = (0,0,0,0)
            z=-50
            linha = f'{i} {j} {z} {cor}\n'
            #linha = f'{i} {j} \n'
            arquivo.write(linha)
            if (j+1) < image1.get_size()[1] and image1.get_at((i,j+1)) == (255,255,255,255):
                z= -40
                linha = f'{i} {j} {z} {cor}\n'
                arquivo.write(linha)
        
    
arquivo.close()


#    pygame.display.update()