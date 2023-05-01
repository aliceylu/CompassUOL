def func(st):
    lista = (list(map(int, st.split(','))))
    soma = sum(lista)
    return soma


A = "1,3,4,6,10,76"
print(func(A))