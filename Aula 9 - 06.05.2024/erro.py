lista = ['a', 'b']

try:
    solucao = 50/2
    solucao2 = lista[10]

except ZeroDivisionError as e:
    print(f'Error: Usuário você teve um erro -> {e}')

except Exception as e:
    print(f'Error diferente: {e}')

else:
    print(f'Solução: {solucao}')