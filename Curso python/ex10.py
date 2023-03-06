def func(lst):
    lista = set(lst)
    return lista


a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(list(func(a)))