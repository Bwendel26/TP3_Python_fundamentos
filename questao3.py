# Escreva um programa em Python que leia um vetor de 10
# palavras e mostre-as na ordem inversa de leitura. (código)

lista = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k"]

def le_ao_contrario(vetor):
    contador = 1
    for i in range(len(vetor)):
        comprimento = len(vetor)
        print(lista[-contador])
        contador += 1

le_ao_contrario(lista)