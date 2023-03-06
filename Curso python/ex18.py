speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
lista = list()

for n in speed.values():
    if n not in lista:
        lista.append(n)
print(list(set(lista)))