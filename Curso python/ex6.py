def func(x, y):
    lista = [i for i in a if i in y]
    return set(lista)


a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(list(func(a, b)))