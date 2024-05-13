mes = int(input("Digite um número referente ao mês: \n"))

match mes:

    case 1:
        print("\nEsse é o mês de Janeiro\n")
    case 2:
        print("\nEsse é o mês de Fevereiro\n")
    case 3:
        print("\nEsse é o mês de Março\n")
    case 4:
        print("\nEsse é o mês de Abril\n")
    case 5:
        print("\nEsse é o mês de Maio\n")
    case 6:
        print("\nEsse é o mês de Junho\n")
    case 7:
        print("\nEsse é o mês de Julho\n")
    case 8:
        print("\nEsse é o mês de Agosto\n")
    case 9:
        print("\nEsse é o mês de Setembro\n")
    case 10:
        print("\nEsse é o mês de Outubro\n")
    case 11:
        print("\nEsse é o mês de Novembro\n")
    case 12:
        print("\nEsse é o mês de Dezembro\n")
    case _:
        print("\nEsse mês não está presente!\n")