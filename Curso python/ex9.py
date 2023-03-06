primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


for e, (n, s, i) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{e} - {n} {s} está com {i} anos')

