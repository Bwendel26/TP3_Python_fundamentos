# Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)

def le_vetor5(lista):
    string_final = ""
    for index in range(5):
        if index == 4:
            string_final += str(lista[index]) + "."
        else:
            string_final += str(lista[index]) + ", "

    print(string_final)

# MAIN
lista = [1, 2, 3, 4, 5]
le_vetor5(lista)