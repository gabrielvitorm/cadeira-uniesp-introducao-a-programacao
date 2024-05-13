num = int(input("Digite o número para saber a tabuada dele: \n"))

for i in range (1, 11):
    with open('Tabuada_3.txt', 'w') as arquivo:
        arquivo.write(f'{num} x {i} = {num*i}\n')