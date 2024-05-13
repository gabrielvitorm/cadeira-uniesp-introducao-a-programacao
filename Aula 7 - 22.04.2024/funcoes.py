def rating_game(qtd_rating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtd_rating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtd_rating}")

qtd_rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(qtd_rating) 

