'''
Solicite ao usuário um valor numérico, inteiro ou real (float), e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler um número e informar se esse número é maior que 10 ou não!\n")

num1 = float(input("Digite um número qualquer: \n"))

if num1 > 10:
    print(f"O {num1} é maior que 10\n")
elif num1 == 10:
    print(f"O {num1} é igual a 10\n")
else:
    print(f"O {num1} é menor que 10\n")

print("--- Finalizando o programa ---\n")