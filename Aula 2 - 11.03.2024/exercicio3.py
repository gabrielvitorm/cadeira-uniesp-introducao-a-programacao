'''
Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler os 2 valores e informar qual o maior entre eles!\n")

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

if num1 > num2:
    print(f"\nO número {num1} é maior que o número {num2}\n")
else:
    print(f"\nO número {num2} é maior que o número {num1}\n")

print("--- Finalizando o programa ---\n")