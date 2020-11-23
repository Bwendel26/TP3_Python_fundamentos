# Usando a biblioteca Pygame, escreva um programa
# que possui uma função que desenha um círculo azul
# de 100 px de diâmetro no centro da tela que se
# move da esquerda para a direita. Sempre que chegar
# na extremidade direita, o círculo deve voltar à extremidade
# esquerda, retomando o movimento da esquerda para a direita.
# (código e printscreen)

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

    pos_x = position[0] / 2
    pos_y = position[1] / 2

    pygame.draw.circle(gameDisplay, blue, (pos_x, pos_y), diametro)

    # Controle de eventos no teclado.

    fim = False
    contadorLeft = 0
    contadorRight = 0
    contadorUp = 0
    contadorDown = 0


    while not fim:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fim = True
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    #codificar movimentacao
                    gameDisplay.fill(black)
                    contadorLeft -= 2
                    pos_x += contadorLeft
                    pygame.draw.circle(gameDisplay, blue, (pos_x, pos_y), diametro)
                #     FUNCIONANDO
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    # codificar movimentacao
                    gameDisplay.fill(black)
                    contadorRight += 2
                    pos_x += contadorRight
                    pygame.draw.circle(gameDisplay, blue, (pos_x, pos_y), diametro)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    # codificar movimentacao
                    gameDisplay.fill(black)
                    contadorUp -= 2
                    pos_y += contadorUp
                    pygame.draw.circle(gameDisplay, blue, (pos_x, pos_y), diametro)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    # codificar movimentacao
                    gameDisplay.fill(black)
                    contadorDown -= 2
                    pos_y -= contadorDown
                    pygame.draw.circle(gameDisplay, blue, (pos_x, pos_y), diametro)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    pass
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    pass
                if event.key == ord('q'):
                    pygame.quit()
                    fim = True

        pygame.display.update()

    pygame.display.quit()
desenha_circulo(100)