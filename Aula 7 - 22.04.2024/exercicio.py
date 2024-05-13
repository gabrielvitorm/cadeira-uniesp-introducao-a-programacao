status = True
herois = []

def add_heroi():
    heroi = input("Digite o nome do herói que você quer adicionar: \n")
    herois.append(heroi)
    print("------ Herói Adicionado -------")

def listar_herois():
    print("------ Heróis Listado -------")
    tamanho_da_lista = len(herois)
    for i in range(tamanho_da_lista):
        print(f"{i + 1} - {herois[i]}")
    print("------ Heróis Listado -------")

def alterar_heroi():
    listar_herois()
    n_heroi = int(input("Escolha o Vingador a ser alterado: \n"))
    if 1 <= n_heroi <= len(herois):
        novo_nome = input("Digite o novo nome do herói: \n")
        herois[n_heroi - 1] = novo_nome
        print("--------- Fim da Alteração do Herói! ---------")
    else:
        print("Índice inválido. Tente novamente.")

def remov_herois():
    listar_herois()
    n_heroi = int(input("Escolha o número do herói a ser removido: \n"))
    if 1 <= n_heroi <= len(herois):
        removido = herois.pop(n_heroi - 1)
        print(f"Herói removido: {removido}")
    else:
        print("Número de herói inválido. Tente novamente.")

while status:
    print("0 - Sair")
    print("1 - Adicionar Herói")
    print("2 - Listar Heróis")
    print("3 - Remover Heróis")
    print("4 - Alterar Herói")
    op = int(input("Digite a opção Desejada: \n"))

    if op == 0:
        print("O programa foi encerrado!")
        break
    elif op == 1:
        add_heroi()
    elif op == 2:
        listar_herois()
    elif op == 3:
        remov_herois()
    elif op == 4:
        alterar_heroi()
    else:
        print("Digite uma opção válida!")