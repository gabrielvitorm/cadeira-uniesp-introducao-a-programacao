'''
## Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

'''
status = True
times = []

# Função para adicionar times a lista
def add_times():
    print("Adicionar times")
    qtd_times = int(input("Digite a quantidade de times que você quer colocar na lista:\n"))
    for i in range(qtd_times):
        val_time = input(f"Digite o nome do {i+1}° Time:\n ")
        times.append(val_time)

# Listar Times
def listar_times():
    print("------ Times Listado -------")
    tamanho_da_lista = len(times)
    for i in range(tamanho_da_lista):
        print(f"{i + 1} - {times[i]}")
    print("------ Times Listado -------")

# Função para remover times da lista5
def rem_times():
    print("------ Remover Times -------")
    listar_times()
    n_time = int(input("Digite o numero do time que você quer remover: \n"))
    if 1 <= n_time <= len(times):
        removido = times.pop(n_time - 1)
        print(f"Herói removido foi:{removido}")
    else:
        print("Número de Time Inválido")

# Adicionar Jogador a um time
def adicionar_jogador():
    listar_times()
    nome_time = input("Digite o nome do time para adicionar o jogador: ")
    qtd_jogadores = int(input("Digite a quantidade de jogadores que você quer adicionar ao time: \n"))
    for i in range(qtd_jogadores):
        if nome_time in times:
            jogador = input(f"Digite o nome do jogador do {i + 1}: ")
            times[nome_time].append(jogador)
        else:
            print("Time não encontrado.")

# Listar Opções de Menu
while status:
    print("0 - Sair")
    print("1 - Adicionar Times")
    print("2 - Listar Times")
    print("3 - Remover Times")
    print("4 - Adicionar Jogador a um time")
    op = int(input("Digite a opção Desejada: \n"))

    if op == 0:
        print("O programa foi encerrado!")
        break
    elif op == 1:
        add_times()
    elif op == 2:
        listar_times()
    elif op == 3:
        rem_times()
    elif op == 4:
        adicionar_jogador()
    else:
        print("Opção Inválida")