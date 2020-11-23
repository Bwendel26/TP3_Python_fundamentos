# Escreva um programa em Python que leia nomes de alunos
# e suas alturas em metros até que um nome de aluno seja
# o código de saída “Sair”. O programa deve possuir uma
# função que indica todos os alunos que tenham altura
# acima da média (a média aritmética das alturas
# de todos os alunos lidos). (código)

def altura_acima_media():
    alunos = []
    nome = ""
    controle = True
    altura = 0.0
    media = 0.0
    soma = 0.0

    while controle:
        nome = str(input("Insira o nome do aluno: "))
        if nome != "Sair":
            altura = float(input("Insira a altura do aluno: "))
            alunos.append([nome, altura])
        elif nome == "Sair":
            controle = False

    for i in range(len(alunos)):
        soma += alunos[i][1]

    media = soma / len(alunos)
    acima_da_media = []

    for i in range(len(alunos)):
        if alunos[i][1] > media:
            acima_da_media.append(alunos[i])

    return acima_da_media

print(altura_acima_media())