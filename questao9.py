# Usando a biblioteca Pygame, escreva um programa que
# possui uma função que desenha um círculo azul de
# 100 px de diâmetro no centro da tela. (código e printscreen)

import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
position = (800, 600)

def desenha_circulo(diametro):
    pygame.init()

    gameDisplay = pygame.display.set_mode(position)
    gameDisplay.fill(black)

    pygame.draw.circle(gameDisplay, blue, (position[0]/2, position[1]/2), diametro)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

desenha_circulo(100)