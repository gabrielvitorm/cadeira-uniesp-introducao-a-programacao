
alunos = [
    ["João", [8, 7, 6]],
    ["Maria", [9, 8, 10]],
    ["Pedro", [7, 8, 7]],
    ["Ana", [6, 5, 8]],
    ["Carlos", [9, 9, 9]],
    ["Mariana", [7, 8, 7]],
    ["José", [10, 9, 8]],
    ["Sofia", [6, 7, 6]],
    ["Rafael", [8, 8, 7]],
    ["Camila", [9, 9, 10]],
    ["Felipe", [7, 6, 7]],
    ["Patrícia", [8, 8, 9]],
    ["Lucas", [9, 10, 9]],
    ["Juliana", [6, 7, 6]],
    ["Paulo", [8, 8, 7]],
    ["Fernanda", [9, 9, 10]],
    ["Gustavo", [7, 6, 7]],
    ["Larissa", [8, 8, 9]],
    ["Mateus", [9, 10, 9]],
    ["Carolina", [6, 7, 6]]
]

for posicao in range(len(alunos)):
    aluno = alunos[posicao]
    soma = 0

    for i in range(len(aluno[1])):
        soma = soma + aluno[1][i]
    media = soma / len(aluno[1])

    print(f"Nome: {aluno[0]} - Média: {media}")


