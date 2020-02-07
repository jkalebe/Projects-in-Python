import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))
rect_pos = (0,0)
mouse = pygame.draw.rect(screen, (255,0,0), Rect(rect_pos, (10,10)))

soma = pygame.image.load('add.png')
subt = pygame.image.load('subtrator.png')
mult = pygame.image.load('multiple.png')
divi = pygame.image.load('division.png')
equal = pygame.image.load('equal.png')

one = pygame.image.load('one.png')
two = pygame.image.load('two.png')
three = pygame.image.load('three.png')
four = pygame.image.load('four.png')
five = pygame.image.load('five.png')
six = pygame.image.load('six.png')
seven = pygame.image.load('seven.png')
eight = pygame.image.load('eight.png')
nine = pygame.image.load('nine.png')
zero = pygame.image.load('zero.png')


soma = pygame.transform.scale(soma, (50,50))
subt = pygame.transform.scale(subt, (50,50))
mult = pygame.transform.scale(mult, (50,50))
divi = pygame.transform.scale(divi, (50,50))
equal = pygame.transform.scale(equal, (50,50))

soma_pos = (400,200)
subt_pos = (500,200)
mult_pos = (400,300)
divi_pos = (500,300)
equal_pos = (500,400)

one_pos = (300,400)
two_pos = (200,400)
three_pos = (100,400)
four_pos = (300,300)
five_pos = (200,300)
six_pos = (100,300)
seven_pos = (300,200)
eight_pos = (200,200)
nine_pos = (100,200)
zero_pos = (100,500)

answer=None
font = pygame.font.SysFont(None,100)
text=font.render(str(answer), False, (255,0,0))


pygame.display.set_caption('Calculadora')
equacao = ''
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            rect_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse.colliderect(soma.get_rect(center=(soma_pos[0]+25, soma_pos[1]+25))):
                equacao = equacao + '+'
            if mouse.colliderect(subt.get_rect(center=(subt_pos[0]+25, subt_pos[1]+25))):
                equacao = equacao + '-'
            if mouse.colliderect(mult.get_rect(center=(mult_pos[0]+25, mult_pos[1]+25))):
                equacao = equacao + '*'
            if mouse.colliderect(divi.get_rect(center=(divi_pos[0]+25, divi_pos[1]+25))):
                equacao = equacao + '/'
            if mouse.colliderect(one.get_rect(center=(one_pos[0]+25, one_pos[1]+25))):
                equacao = equacao + '1'
            if mouse.colliderect(two.get_rect(center=(two_pos[0]+25, two_pos[1]+25))):
                equacao = equacao + '2'
            if mouse.colliderect(three.get_rect(center=(three_pos[0]+25, three_pos[1]+25))):
                equacao = equacao + '3'
            if mouse.colliderect(four.get_rect(center=(four_pos[0]+25, four_pos[1]+25))):
                equacao = equacao + '4'
            if mouse.colliderect(five.get_rect(center=(five_pos[0]+25, five_pos[1]+25))):
                equacao = equacao + '5'
            if mouse.colliderect(six.get_rect(center=(six_pos[0]+25, six_pos[1]+25))):
                equacao = equacao + '6'
            if mouse.colliderect(seven.get_rect(center=(seven_pos[0]+25, seven_pos[1]+25))):
                equacao = equacao + '7'
            if mouse.colliderect(eight.get_rect(center=(eight_pos[0]+25, eight_pos[1]+25))):
                equacao = equacao + '8'
            if mouse.colliderect(nine.get_rect(center=(nine_pos[0]+25, nine_pos[1]+25))):
                equacao = equacao + '9'
            if mouse.colliderect(zero.get_rect(center=(zero_pos[0]+25, zero_pos[1]+25))):
                equacao = equacao + '0'
            if mouse.colliderect(equal.get_rect(center=(equal_pos[0]+25, equal_pos[1]+25))):
                num1 = int(equacao[0])
                num2 = int(equacao[2])

                if equacao[1] == '+':
                    equacao = equacao + '=' + str(num1 + num2)
                if equacao[1] == '-':
                    equacao = equacao + '=' + str(num1 - num2)
                if equacao[1] == '*':
                    equacao = equacao + '=' + str(num1 * num2)
                if equacao[1] == '/':
                    equacao = equacao + '=' + str(num1 / num2)
                

    screen.fill((200,200,200))

    screen.blit(soma, soma_pos)
    screen.blit(subt, subt_pos)
    screen.blit(mult, mult_pos)
    screen.blit(divi, divi_pos)
    screen.blit(equal, equal_pos)

    screen.blit(one, one_pos)
    screen.blit(two, two_pos)
    screen.blit(three, three_pos)
    screen.blit(four, four_pos)
    screen.blit(five, five_pos)
    screen.blit(six, six_pos)
    screen.blit(seven,seven_pos)
    screen.blit(eight, eight_pos)
    screen.blit(nine, nine_pos)
    screen.blit(zero, zero_pos)

    mouse = pygame.draw.rect(screen, (255,0,0), Rect(rect_pos, (10,10)))

    answer = equacao
    text = font.render(str(answer), False, (255,0,0))
    screen.blit(text, (100,40))

    pygame.display.update()
