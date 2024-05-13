'''
Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável x. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
'''

A = []
X = 0
M = []
num = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}° número do vetor A:\n"))
    A.append(num)

for j in range(1):
    X = int(input("Digite o vetor X: \n"))

for num in A:
    resultado = num * X
    M.append(resultado)

print(f"Vetor A:{A}")
print(f"Vetor M (resultante da multiplicação de A por X): {M}")
