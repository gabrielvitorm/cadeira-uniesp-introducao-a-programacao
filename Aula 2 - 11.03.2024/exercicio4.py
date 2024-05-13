'''
Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler os 2 valores e colocar em ordem crescente!\n")

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

if num1 > num2:
    print(f"\n{num2}, {num1}\n")
else:
    print(f"\n{num1}, {num2}\n")

print("--- Finalizando o programa ---\n")