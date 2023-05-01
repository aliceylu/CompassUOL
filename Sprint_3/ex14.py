def func(*args, **kwargs):
    for argumento in args:
        print(argumento)
    for valor in kwargs.values():
        print(valor)


func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
