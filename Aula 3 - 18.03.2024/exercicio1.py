'''# Inicializa uma lista para armazenar os números que atendem à condição
numeros = []

# Loop pelos números de 1000 a 2000
for num in range(1000, 2001):
    # Verifica se o resto da divisão por 11 é igual a 5
    if num % 11 == 5:
        numeros.append(num)  # Adiciona o número à lista

# Imprime os números que atendem à condição
print("Números entre 1000 e 2000 que produzem resto 5 ao dividir por 11:")
print(numeros)
'''
numero = 0

for num in range (1000, 2001):
    if num % 11 == 5:
        print(f"O {num} dividido por 11 tem sobra de 5")