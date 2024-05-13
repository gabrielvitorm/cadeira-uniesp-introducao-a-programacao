print("--- Iniciando o programa ---")

idade = int(input("Digite a sua idade:\n"))
idade_nova = idade + 1

if idade > 17: 
    print(f"\nPode entrar na festa, pois você já tem {idade} anos\n")
elif idade > 16 and idade < 18:
    print("\nÉ hora de voltar para sua casa")
else:
    print(f"\nVocê ainda não pode entrar na festa, pois você ainda tem {idade} anos, vou chamar seus pais.\n")

print("\n--- Finalizando o programa ---")