# 10. Crie uma constante chamada PI com valor 3.14 e peça ao usuário o raio de um círculo. Em seguida, calcule o perímetro do círculo.

pi = 3.14

print("\nEsse programa calcula o perímetro de um circulo a partir do valor do Raio dele\n")
r = float(input("Digite o Raio do Circulo:\n"))

peri = 2*pi*r

print(f"O valor do perímetro de um circulo com raio {r}, vai ser igual a {peri}\n")
