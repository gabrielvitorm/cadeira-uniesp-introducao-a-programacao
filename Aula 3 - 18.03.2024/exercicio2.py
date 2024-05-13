def calcular_tabuadas():

    with open("tabuadas.txt", "w") as arquivo:
        
        for num in range(1, 11):
            arquivo.write(f"Tabuada do {num}:\n")
            
            for mult in range(1, 11):
                resultado = num * mult
                arquivo.write(f"{num} x {mult} = {resultado}\n")
            arquivo.write("\n") 

    print("Tabuadas calculadas e salvas no arquivo 'tabuadas.txt'.")

calcular_tabuadas()

