# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
# c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
# d. Modifique sua lista, substitua os desistentes por novos convidados.
# e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ['Neymar', 'Cristiano Ronaldo', 'Messi', 'Payet', 'Mike Tyson']

for convidado in convidados:
    print(f'Olá, {convidado}! Você foi convidado para uma festa exclusiva em João Pessoa!')

desistente = 'Neymar'
print(f'\n{desistente} acabou de confirmar que não vem a festa\n')

convidados.remove('Neymar')
convidados.append('Dan Bilzerian')

for convidado in convidados:
    print(f'Olá, {convidado}! Você foi convidado para uma festa exclusiva em João Pessoa!')