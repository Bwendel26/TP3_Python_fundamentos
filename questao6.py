# Escreva um programa em Python que leia diversas
# frases até a palavra “Sair” ser digitada.
# Indique quais frases apresentam a palavra “eu”. (código)

def frases_com_eu():
    controle = True
    frase = ""
    frases = []
    frases_finais = []

    while controle:
        if frase == "Sair":
            controle = False
        else:
            frase = str(input("Entre com uma frase: "))
            frases.append(frase)

    for i in range(len(frases)):
        frase_atual = frases[i].split()
        for j in range(len(frase_atual)):
            if frase_atual[j] == "eu" or frase_atual[j] == "Eu":
                frases_finais.append(frases[i])
                print(frases[i])


    return frases_finais

frases_com_eu()
