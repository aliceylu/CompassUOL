for i in range(0, 3):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        print(f'Par: {n}')
    elif n % 2 != 0:
        print(f'Ímpar: {n}')