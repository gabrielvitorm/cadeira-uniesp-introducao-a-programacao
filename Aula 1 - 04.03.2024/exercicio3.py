# 3. Escreva um programa que solicite ao usuário dois números e imprima a soma deles.

line = "="

print("Escreva 2 números e o programa vai somar esses 2 números")
print(line * 25)

num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))

sum = num1 + num2

print(f"A soma dos 2 números é igual a {sum}")