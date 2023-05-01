caminho = 'estudantes.csv'
with open(caminho, 'r') as arquivo:
    lista = []
    linha = [[col.strip('\n') for col in row.split(',')] for row in arquivo]
    for linha1 in sorted(linha, key=lambda x: x[0]):
        lista.append(linha1)

for n in lista:
    notas = [int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5])]
    notas = (sorted(notas, reverse=True)[:3])
    notas1 = map(float, notas)
    media = sum(notas1) / 3
    print(f'Nome: {n[0]} Notas: {notas} Média: {round(media, 2)}')