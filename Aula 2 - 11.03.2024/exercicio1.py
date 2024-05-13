'''
Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é aprovado). Escrever também o resultado da média calculada.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler sua primeira e sua segunda nota e fazer a média e informar se você foi aprovado ou não!\n")

nota1 = float(input("Digite a sua primeira nota: \n"))

nota2 = float(input("Digite a sua segunda nota: \n"))

media = (nota1 + nota2)/2

if media > 6:
    print(f"Parabéns, você foi aprovado e sua média foi de {media}\n")
else:
    print(f"Infelizmente você foi reprovado, sua média foi de {media}\n")

print("--- Finalizando o programa ---\n")