# Escreva um programa em Python que realiza operações
# de inclusão e remoção em listas. Seu programa deve
# perguntar ao usuário qual operação deseja fazer: (código)

    # Mostrar lista;
    # Incluir elemento;
    # Remover elemento;
    # Apagar todos os elementos da lista.

# Se a opção for a alternativa (a), seu programa deve
# apenas mostrar o conteúdo da lista. Se a opção for a
# alternativa (b), seu programa deve pedir o valor do
# elemento a ser incluído. Se a opção for a alternativa (c),
# seu programa deve pedir o valor do elemento a ser removido.
# E se a opção for a alternativa (d), deve-se apenas exibir
# se a operação foi concluída.

elementos = ["Bruno", "Gabi"]

def mostrar_lista(lista):
    print("\n\n")
    print(lista)
    print("\n\n")

def incluir_lista(lista, objeto):
    return lista.append(objeto)

def remover_lista(lista, objeto):
    return lista.remove(objeto)

def apagar_lista(lista):
    for i in lista:
        return lista.pop()

def principal(lista):

    fechar = False

    while not fechar:
        print("Escolha as seguintes opcoes:\n"
              "(a) para mostrar a lista.\n"
              "(b) para incluir um elemento a lista.\n"
              "(c) para remover um elemento da lista.\n"
              "(d) para excluir todos os elementos da lista.\n"
              "(Sair) para sair do programa.\n")

        entrada = str(input("Entre com seu comando: "))

        if entrada == "a" or entrada == "A":
            mostrar_lista(lista)
        elif entrada == "b" or entrada == "B":
            objeto = input("Entre com o objeto a ser adicionado na lista: ")
            incluir_lista(lista, objeto)
        elif entrada == "c" or entrada == "C":
            objeto = input("Entre com o objeto a ser removido da lista: ")
            remover_lista(lista, objeto)
        elif entrada == "d" or entrada == "D":
            apagar_lista(lista)
            print("Operacao concluida!")
        elif entrada == "sair" or entrada == "Sair":
            fechar = True
        else:
            print("Comando invalido!")

principal(elementos)