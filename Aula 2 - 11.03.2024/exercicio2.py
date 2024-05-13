'''
Escreva um programa que verifique se um número é maior, menor ou igual a 50.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler o número que você digitar e informar se o número é maior, menor ou igual a 50!\n")

num1 = int(input("Digite um número inteiro da sua escolha\n"))

if num1 > 50:
    print(f"O número {num1} é maior que 50!\n")
elif num1 < 50:
    print(f"O número {num1} é menor que 50!\n")
else:
    print(f"O número {num1} é igual a 50!\n")

print("--- Finalizando o programa ---\n")