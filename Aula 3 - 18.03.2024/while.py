spam = 0
while spam <= 100:
    print(f'Hello, world. Número: {spam}')
    spam = spam + 2

    if (spam % 2) > 0:
        spam = spam -1