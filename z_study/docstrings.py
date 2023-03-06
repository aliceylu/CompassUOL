"""Documentando funções com Docstrings"""

def diz_oi():
    """Uma função simples que retorna a string 'Oi'!"""
    return 'Oi!'

print(diz_oi()) 

# É possível acessar documentação de uma função.
# utilizando print(diz_oi.__doc__)
#help(diz_oi)

# args - não é obrigatório

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total
print(soma_todos_numeros())


# ou

def soma_todos_numeros(*args):
    return sum(args)
print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))


def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Amanda', 'Souza'))
print(soma_todos_numeros('Ana', 'Maria' 1))
print(soma_todos_numeros(2, 3))



def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo, Geek'
    return 'Não tenho certeza quem você é'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


# **kwargs - não é obrigatório também.

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))


"""
Nas funções, podemos ter NESTA ORDEM:

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""

def minha_funcao(idade, nome, args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)