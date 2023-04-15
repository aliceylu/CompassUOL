"""Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas o ano em que ele completará 100 anos.
Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem').
Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas."""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cent = (100 - idade) + 2023
print(cent)

"""Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares. 
Para cada número, imprima o Par: ou Ímpar: e o número correspondente.
Exemplo de formato de saída:
Par: 2
Ímpar: 3
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


if n1 % 2 == 0:
    print('Par: {}'.format(n1))
elif n1 % 2 != 0:
    print('Ímpar: {}'.format(n1))

if n2 % 2 == 0:
    print('Par: {}'.format(n2))
elif n2 % 2 != 0:
    print('Ímpar: {}'.format(n2))

if n3 % 2 == 0:
    print('Par: {}'.format(n3))
elif n3 % 2 != 0:
    print('Ímpar: {}'.format(n3))


primos = []
for i in range(0, 100):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
        else:
            primos.append(i)
return primos
lista_primos = num_primos(100)
print(*lista_primos, '\n')


primos = (0, 100)
for i in primos:
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
        else:
            primos.append(i)
return primos
lista_primos = num_primos(100)
print(*lista_primos, '\n')

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')



# 19
import random

random_list = random.sample(range(500), 50)
random_list.sort()

mediana = 0
media = 0
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(valor_maximo)
print(valor_minimo)

