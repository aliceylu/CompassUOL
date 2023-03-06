def div(alist, parts=3):
    length = len(alist)
    return ' '.join(map(str, [alist[i*length // parts: (i+1)*length // parts]
             for i in range(3)]))


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(div(lista))