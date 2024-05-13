clubes = []

quantidade_times = int(input("Digite quantos times você quer colocar na lista: \n"))

for i in range(quantidade_times):
    nome_clube = input("Digite o nome do clube que você quer adicionar a lista: \n")
    clubes.append(nome_clube)

print(f"Os clubes da lista são {clubes}\n")

print("Agora digite o nome de um time que você quer procurar na lista\n")

pesquisado = input("Digite o nome do clube para pesquisar\n")

for clube in clubes:
    if pesquisado == clube:
        print(f"O clube {pesquisado}, está na lista")
    else:
        print(f"Não achei! O clube {pesquisado}, não está na lista!")
