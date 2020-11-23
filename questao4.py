# Escreva um programa em Python que leia um vetor
# de números de tamanho t. Leia t previamente.
# Em seguida, faça seu programa verificar
# quantos números iguais a 0 existem nele. (código)

lista = [1, 2, 1, 3, 2, 0, 0]

def nums_iguais(vetor):
    qtd_iguais = 0
    for index1 in range(len(vetor)):
        atual = vetor[index1]
        if atual == 0:
            qtd_iguais += 1
        # for index2 in range(len(vetor)):
        #     comparado = vetor[index2]
        #     if atual == comparado:
        #         qtd_iguais += 1

    return qtd_iguais

print(nums_iguais(lista))