# Usando Python, faça o que se pede (código e printscreen):
#
#     Crie uma lista vazia;
#     Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
#     Imprima a lista;
#     Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
#     Imprima a lista modificada;
#     Imprima também o tamanho da lista usando a função len();
#     Altere o valor do último elemento para 6 e imprima a lista modificada.

# Vars
lista = list()

# funcs
def add_list(elementos):

    for elemento in elementos:
        lista.append(elemento)

    print(lista)

def check_and_remove_from_list(elementos, remover):

    for elemento in elementos:
        for num in remover:
            if elemento == num:
                lista.remove(elemento)

    print(lista)

def change_last(elementos, mod):

    lista[len(lista) - 1] = mod

    print(lista)

# MAIN
remover = [3, 6]
elementos = [1, 2, 3, 4, 5]
add_list(elementos)
check_and_remove_from_list(elementos, remover)
print(len(lista))
change_last(elementos, 6)