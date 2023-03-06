def my_map(lista, f):
    return(list(map(f, lista)))
    
    
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = (lambda x: x**2)

print(my_map(lista1, func))