"""
Funções com parametro (de entrada)
Recebem dados para serem processados dentro da mesma.

Em um programa, geralmente temos:

entrada -> processamento -> saída

Em funções, temos:
-Não possuem entrada;
-Não possuem saída;
-Não possuem entrada mas não possuem saída;
-Não possuem entrada mas possuem saída;
-Possuem entrada e saída.

"""

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

#sempre retorna o mesmo resultado. Não possui nenhuma entrada e o processamento é o mesmo.
#refatorando:

def quadrado(numero):
    return numero * numero

def quadrado(numero1):
    return numero1 ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
#ou
ret = quadrado(6)
print(ret)

#refatorando:

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('etc... {aniversariante}!')

cantar_parabens('Nome')


#Funções podem ter n parametros de entrada. Podemos receber como entrada em uma função
#quantos parametros forem necessários. Eles são separados por vírgulas.

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2,5))
print(multiplica(4,5))
print(outra{3, 2, msg})
#mensagem vi ser impressa no resultado da equação.



#NOMEANDO PARAMETROS

def nome_completo(string1,string2):
    return f'Seu nome completo é {string1} {string2}'

print(nome_completo('Ana', 'Maria'))

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


"""
PARÂMETROS E ARGUMENTOS:

Parâmetros são variáveis declaradas na definição de uma função;
Argumentos são dados passados durante a execução de uma função.

Parâmetro na função, argumento no print.

A ordem dos parâmetros importa.

Argumentos nomeados (keyword arguments)

Caso utilizemos nome dos parâmetros nos argumentos para informá-los, 
podemos utilizar qualquer ordem

"""

print(nome_completo(nome='Ana', sobrenome='Maria'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))


"""
Erro comum no RETURN

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

-resultado:16

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total

tupla = (1, 2, 3, 4, 5, 6, 7) (ou sem parenteses)
print(soma_impares(tupla))

-resultado:1
"""

def exponencial(numero, potencia=2):
    return numero ** potencia
##potência não precisa ter valor informado
print(exponencial(3))
print(exponencial(3, 5))

"""Incorreto = def teste(num=2, potencia)   /  non default sempre no final"""

"""
Variáveis locais tem preferência sobre variáveis globais.

ex.:

instrutor = 'Geek'
def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor)'

print(diz_oi())

resultado: Oi Python

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'

-não é possível dar print somente na variável prof


De preferência evitar variáveis globais.

total = 0

def incrementa():
    total = total + 1
    return total

print(incrementa())

-irá dar erro pois variável local se sobrepôs


total = 0

def incrementa():
    global total (chamando variável global)
    total = total + 1
    return total

print(incrementa())


"""

"""


def fora():
    contador = 0

def dentro():
    nonlocal contador
    contador = contador + '
    return contador
return dentro()



"""











