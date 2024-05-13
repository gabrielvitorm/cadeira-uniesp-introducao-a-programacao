#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

# Lista para armazenar os cadastros de usuários
usuarios = []

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o e-mail do usuário: ")

    # Cria um dicionário com os dados do usuário
    usuario = {"Nome": nome, "Idade": idade, "Email": email}
    usuarios.append(usuario)

# Realiza o cadastro de três usuários
for _ in range(3):
    cadastrar_usuario()

# Exibe todos os usuários cadastrados
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['Nome']}, Idade: {usuario['Idade']}, E-mail: {usuario['Email']}")
