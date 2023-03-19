caminho = 'number.txt'
with open(caminho, 'r') as arquivo:
    lista = []
    for index, line in enumerate(arquivo):
        if index > 0:
            lista.append(line)

lista = list(map(int, lista))
orden = (sorted(lista, reverse=True))
pares = (lambda x: x % 2 == 0)
resultpares = (list(filter(pares, orden)))
print(resultpares[:5])
print(sum(resultpares[:5]))