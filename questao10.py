# Usando a biblioteca Pygame, escreva um programa
# que possui uma função que desenha um quadrado
# vermelho de 100 px de lado no centro da tela.
# O quadrado deve ser capaz de se movimentar
# vertical e horizontalmente através de teclas
# do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as
# setas do teclado. (código e printscreen)

import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
position = (800, 600)


def desenha_quadrado(lado):
    pygame.init()

    gameDisplay = pygame.display.set_mode(position)
    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, red, (position[0]/2 - lado/2, position[1]/2 - lado/2, lado, lado))

    # Controle de eventos no teclado.

    fim = False
    contadorLeft = 0
    contadorRight = 0
    contadorUp = 0
    contadorDown = 0

    pos_x = position[0] / 2
    pos_y = position[1] / 2

    while not fim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fim = True
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    #codificar movimentacao
                    contadorLeft -= 2
                    gameDisplay.fill(black)
                    pygame.draw.rect(gameDisplay, red, (position[0]/2 - lado/2 + contadorLeft, position[1]/2 - lado/2, lado, lado))
                #     FUNCIONANDO
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    # codificar movimentacao
                    contadorRight += 2
                    gameDisplay.fill(black)
                    pygame.draw.rect(gameDisplay, red, (position[0] / 2 - lado / 2 + contadorRight, position[1] / 2 - lado / 2, lado, lado))
                if event.key == pygame.K_UP or event.key == ord('w'):
                    # codificar movimentacao
                    contadorUp -= 2
                    gameDisplay.fill(black)
                    pygame.draw.rect(gameDisplay, red, (position[0] / 2 - lado / 2, position[1] / 2 - lado / 2 + contadorUp, lado, lado))
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    # codificar movimentacao
                    contadorUp += 2
                    gameDisplay.fill(black)
                    pygame.draw.rect(gameDisplay, red, (position[0] / 2 - lado / 2, position[1] / 2 - lado / 2 + contadorDown, lado, lado))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    return "stop"
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    return "stop"
                if event.key == ord('q'):
                    pygame.quit()
                    fim = True

        pygame.display.update()

desenha_quadrado(100)