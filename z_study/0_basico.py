#Comandos básicos Python

print('Mensagem')
#Resultado: Mensagem

print(7 + 4)
#Resultado: 11

print('7' + '4')
#Resultado: 74

print('Olá' + 5) #errado
print('Olá', 5) #correto

#Variáveis - lower case ( "=" recebe)

nome = 'Alice'
idade = '27'
cidade = 'Ponta Grossa'

print(nome, idade, cidade)


#input

dd = input('Dia = ')
mm = input('Mes = ')
aa = input('Ano = ')
print('Você nasceu no dia' ,dd, 'de' ,mm, 'de' ,aa, '.Correto?')



"""Tipos primitivos e saída de dados
nome = input('Qual o seu nome? ')
print('Bem vindo(a), ',nome)

nome = input('Qual o seu nome? ')
print('Bem vindo(a), {}!'.format(nome))


n1 = input('Digite um número:')
n2 = input('Digite outro número:')
s = n1 + n2
print('A soma vale' , s)

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
#print('A soma entre' ,n1, 'e' ,n2, 'vale: {}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
print('A soma vale {}'.format(n1+n2))

"""
"""
type(x) #tipo primitivo
x.isspace() #Somente espaços
x.isnumeric() #É um número
x.isalpha() #Alfabético
x.isaslnum() #Alfanumérico
x.isupper() #maiuscula
x.islower() #minuscula
x.istitle() #capitalizada"""

"""Ordem de precedência operações aritméticas:
1 - ()
2 - ** potência / ou pow(i,j)
3 - * , / , // , %
4 - + , -

raiz quadrada:
81**(1/2) / 127**(1/3)
"""
print('Mensagem {:20}'.format(nome)) #irá escrever o nome em 20 espaços.
#{:>20} alinhamento à direita.
#{:^20} centralizado
#{:=^20} centralizado entre =

"""n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.9f}'.format(s, m, d), end='')
print('Divisão inteira {} e potência {}'.format(di, e))


n1 = int(input('Digite um valor: '))
s = (n1 + 1)
a = (n1 - 1)
print('O sucessor do número digitado é: {}, e o antecessor é: {}'.format(s, a))

n1 = int(input('Digite um valor: '))
d = (n1 * 2)
t = (n1 * 3)
r = (n1 ** (1/2))
print('O dobro do valor escolhido é {}, o triplo é {} e sua raíz quadrada é {}'.format(d, t, r))



n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
print('A média das notas é: {:.1f}.'.format((n1 + n2) / 2))

m = int(input('Digite um valor em metros: '))
c = m * 100
mm = m * 1000
print('O valor escolhido convertido em centímetros é {}, e em milimetros é {}'.format(c, mm))


n1 = int(input('Digite um número: '))
print('{} x 1 = {}'.format(n1, n1))
print('{} x 2 = {}'.format(n1, (n1 * 2)))
print('{} x 3 = {}'.format(n1, (n1 * 3)))
print('{} x 4 = {}'.format(n1, (n1 * 4)))
print('{} x 5 = {}'.format(n1, (n1 * 5)))
print('{} x 6 = {}'.format(n1, (n1 * 6)))
print('{} x 7 = {}'.format(n1, (n1 * 7)))
print('{} x 8 = {}'.format(n1, (n1 * 8)))

print('-' * 12)
print('{} x {:2} = {}'.format(n1, 1, n1*1))
print('{} x {:2} = {}'.format(n1, 2, n1*2))
print('{} x {:2} = {}'.format(n1, 3, n1*3))
print('{} x {:2} = {}'.format(n1, 4, n1*4))
print('{} x {:2} = {}'.format(n1, 5, n1*5))
print('-' * 12)


l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
ar = l * a
t = ar / 2
print('A área em metros a ser pintada é {}, e a quantidade necessária de tinta em litros é {}'.format(ar, t))


Solicitar um valor e retornar novo valor com 5% de desconto
p1 = int(input('Digite o preço: '))
d = (p1 / 100) * 5
print('O valor com desconto será: {}'.format(p1 - d))


s = int(input('Digite o valor do salário: '))
a = (s / 100) * 15
print('O valor do salário com aumento será {}'.format(s + a))

dias = float(input('Quantos dias? '))
km = float(input('Quantos km? '))
vdias = dias * 60
vkm = km * 0.15
print('O valor total a ser pago será de R${:.2f}'.format(vdias + vkm))

BIBLIOTECA MATH (import) / from math import sqrt, ceil
ceil (arredondar ^), floor (arredondar baixo)
trunc (eliminar ultimo num)
pow (potencia)
sqrt (raiz quadrada)
factorial

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem será: ')
print(lista)

import pygame
pygame.init()
pygame.mixer.music.load('nome_arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()


""""##Ler nome completo e mostre nome com todas as letras maiusculas e minusculas
## quantas letras ao todo sem espaços e quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em upper case é {}'.format(nome.upper()))
print('Seu nome em lower case é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

Ler um número e mostrar dígitos separados.

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


-ler o nome de uma cidade e dizer se começa ou não com "Santo"

cid = str(input('Cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')


-dizer se o nome tem "silva"

nome = str(input('Nome completo: ')).strip()
print('O nome tem Silva? {}'.format('silva' in nome.lower()))


-ler uma frase / quantas vezes aparece a letra "a" / em que posição aparece pela primeira vez / posição última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))

-separar nomes, dizer somente primeiro e último nome

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



----------
programa escolhe número entre 0 e 5, usuário tenta adivinhar

from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input('Qual o número escolhido? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você acertou.')
else:
    print('O número que eu havia escolhido foi {} e não o {}.format(computador, jogador))

--------
-ler a velocidade de um carro. se ele ultrapassar 80km/h, mostrar mensagem com valor da multa
R$7,00 para cada km acima

vel = int(input('Qual a velocidade? '))
    if vel > 80:
        multa = (vel - 80) * 7
        print('Você foi multado. O valor da multa será de R${}.'.format(multa))
    else:
        print('Você estava dentro do limite de velocidade.')

dist = float(input('Digite a distância: '))
if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.50
print('Sua viagem custará: {}'.format(valor))

#ano bissexto
from datetime import date
ano = int(input('Ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

    

#Ler 3 num e mostre qual o maior e o menor

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))


#perguntar salário, acima de 1250 aumento de 10%, abaixo ou igual de 15%

sal = float(input('Digite o salário: '))
if sal > 1250:
    aumento = (sal * 10 / 100) + sal
if sal <= 1250:
    aumento = (sal * 15 / 100) + sal
print('O salário com aumento será de R${}'.format(aumento))


#3 seguimentos formam triângulo? uma das retas tem que ser menor do que a soma das outras duas retas.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')

padrão ANSI

\033[style;text;background m
\033[0;33;44m

style: 0 - none / 1 - bold / 4 - underline / 7 - negative
text: 30 ao 37
back: 40 ao 47

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a, b))

print('Olá, {}{}{}'.format('\033[d;34m', nome, '\033[m'))

nome = 'tal'
cores = {'limpa';'\033[m',
        'azul';'\033[34m',
        'amarelo';'\033[33m',
        'pretoebranco';\033[7;30m'}

print('Olá, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
"""




