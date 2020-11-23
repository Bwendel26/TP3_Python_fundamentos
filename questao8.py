# Faça uma função um programa em Python que simula um
# lançamento de dados. Lance o dado 100 vezes e
# armazene os resultados em um vetor. Depois, mostre
# quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores (1-6) e uma função
# do módulo 'random' de Python para gerar números
# aleatórios, simulando os lançamentos dos dados. (código)

from random import randint

lancamentos = []
dado_lados = 6

def lanca_dados(tipo_dado):

    # define a quantidade de lados do dado, criando sub-vetores
    for i in range(tipo_dado):
        lancamentos.append([])

    for i in range(100):
        dado = randint(1, tipo_dado)
        lancamentos[dado - 1].append(dado)

    lista_demonstracao = []

    for i in range(len(lancamentos)):
        atual = lancamentos[i][0]
        contador = 0
        for j in range(len(lancamentos[i])):
            contador += 1
        lista_demonstracao.append([atual, contador])

    for i in range(len(lista_demonstracao)):
        print("O número {} foi tirado {} vezes.".format(lista_demonstracao[i][0], lista_demonstracao[i][1]))

lanca_dados(dado_lados)