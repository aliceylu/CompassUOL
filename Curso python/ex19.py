import random
random_list = random.sample(range(500),50)
random_list.sort()

media = (sum(random_list) / len(random_list))
valor_minimo = min(random_list)
valor_maximo = max(random_list)
for n in random_list:
    n = len(random_list)
    if n % 2 == 0:
        m1 = random_list[n//2]
        m2 = random_list[n//2 - 1]
        mediana = (m1 + m2) / 2

print(f'Media: {media:}, Mediana: {mediana:}, Mínimo: {valor_minimo:}, Máximo: {valor_maximo:}')
