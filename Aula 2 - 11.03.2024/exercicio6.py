'''
Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
'''
print("--- Iniciando o programa ---")
print("O programa vai ler seu saldo, seu débito e crédito, e vai entregar o saldo atual!\n")

saldo = float(input("Digite o seu saldo inicial: \n"))
debito = float(input("Digite quanto foi o seu débito: \n"))
credito = float(input("Digite quanto foi o seu crédito: \n"))

saldo_atual = saldo - (debito + credito)

if saldo_atual >= 0:
    print(f"\nO seu saldo R${saldo_atual} é positivo!")
else:
    print(f"\nO seu saldo R${saldo_atual} é negativo")

print("--- Finalizando o programa ---\n")