"""
salario = float(input('Digite seu salário: '))
valor = float(input('Digite o valor da casa: '))
anos = int(input('Digite em quantos anos vai pagar: '))
prestacao = (valor / (anos * 12))
if prestacao > (salario * 30 / 100):
    print('A prestação ultrapassa 30%.')
else:
    print('A prestação será de {}.'.format(prestacao))

    
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1 + n2) / 2 < 5.0:
    print('Reprovado.')
if (n1 + n2) / 2 > 7.0:
    print('Aprovado.')
else:
    print('Recuperação')


if 7 > media )= 5:
    print('Recuperação')

    

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}.format(num, hex(num)))
else:
    print('Opção inválida.')


for c in range(6, 0, -1):
    print(c)
resultado: 6 5 4 3 2 1 0

for c in range(0, 7, 2):
    print(c)
resultado: 0 2 4 6

for c in range(0,3):
    n = int(input('Digite um valor: '))
print('fim')
-irá imprimir "digite um valor" 3x


- impares e múltiplos de 3, somados e contados

soma = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0:
        if c % 2 != 0:
            soma = soma + c
            cont = cont + 1
print('Soma: {}, cont: {} '.format(soma, cont))



-tabuada (for)

n1 = int(input('Digite um número: '))
for c in range(1, 11):
    result = c * n1
    print('{} x {} = {}'.format(c, n1, result))    

print('{} x {:2} = {}'.format(n1, c, n1*c))


-solicitar 6 números e somar somente os pares
s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print('O somatório dos valores pares é: {}'.format(s))

-contagem regressiva
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
sleep(0.5)
print('pow')

-pares de 1 a 50
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')

        


-progressão aritmética
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end='>')

    
-numeros primos

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo')

ou
inverso = junto[::-1]


-ler data nasc 7 pessoas

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0 
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade'.format(totmaior, totmenor))



-ler peso de 5 pessoas mostrar maior e menor

maior = 0
menor = 0
for p in range(1, 6):
    peso = floar(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kgs e o menor foi de {}kgs.'.format(maior, menor))

-pedir nome, sexo e idade de 4 pessoas. dizer x mulheres tem menos de 20 anos
quantos anos e nome do homem mais velho

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('{}ª Pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))



sexo = str(input('Sexo: [M/F]')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Tente novamente'))



from random import randint
count = 0
computador = randint(0, 10)
jogador = int(input('Adivinhe o número entre 0 e 10: '))
while jogador != computador:
    count += 1
    jogador = int(input('Tente novamente: '))
else:
    print('Você acertou em {} tentativas.'.format(count))

    

from random import randint
computador = randint(0, 10)
acertou = False
count = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    count += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas.'.format(count))


menu = str([1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print(menu)
opt = int(input('Escolha uma opção do menu: '))
while opt != 5:
    if opt == 1:
        soma = n1 + n2
        print('O resultado da soma de {} e {} é: {}'. format(n1, n2, soma))
    elif opt == 2:
        mult = n1 * n2
        print('O resultado a multiplicação entre {} e {} é: {}'.format(n1, n2, mult))
    elif opt == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opt == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim.')

n = int(input('Digite um número p calcular seu fatorial:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-=1
print('{}'.format(f))


-PA + pergunta de mais termos

print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer visualizar a mais?))
print('Progressão finalizada com {} termos mostrados.'.format(total))


-sequência de fibonacci
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> fim')



-ler vários números, 999 para parar sem somar/contar
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))



-ler vários numeros, mostrar média e qual maior e menor

resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor: menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'. format(maior, menor))

num = soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += num
    cont += 1
print(f'A soma vale {soma} e {cont} números foram digitados.')


----------
tabuada
tab = 0
while True:
    num = int(input('Digite um valor: '))
    if num > 0:
        for tab in range(1, 11):
            print(f'{tab} x {num} = {tab * num}')
            tab += 1
    if num < 0:
        print('Fim.')
        break


    ---
    jogar contra computador par ou impar
from random import randint
computador = randint(0, 10)
pessoa = parimpar = cont = 0
soma = computador + pessoa
while True:
    pessoa = int(input('Digite um número:'))
    parimpar = str(input('Par ou ímpar? '))
    if (soma) % 2 == 0:
        if parimpar in 'Pp':
            cont += 1
            print(f'Você jogou {pessoa} e o pc {computador}. O total foi de {pessoa + computador}. Você ganhou um total de {cont} vezes.')
        if parimpar in 'Ii':
            print(f'Você perdeu. Você jogou {pessoa} e o pc {computador}. O total foi de {pessoa + computador}.')
            break
    if (soma) % 2 != 0:
        if parimpar in 'Ii':
            cont += 1
            print(f'Você jogou {pessoa} e o pc {computador}. O total foi de {pessoa + computador}. Você ganhou um total de {cont} vezes.')
        if parimpar in 'Pp':
            print(f'Você perdeu. Você jogou {pessoa} e o pc {computador}. O total foi de {pessoa + computador}.')
            break
else:
    print('Fim')



    ------
    digitar valores e produtos somar total
soma = 0
while True:
    prod = str(input('Digite o produto: '))
    price = float(input('Digite o valor: R$'))
    cont = str(input('Quer continuar? [S/N] '))
    soma += price
    if cont in 'Ss':
        prod = str(input('Digite o produto: '))
        price = float(input('Digite o valor: R$'))
        cont = str(input('Quer continuar? [S/N] '))
        soma += price

    if cont in 'Nn':
        print(f'O valor total gasto foi de R${soma}.')
        break

else:
    print('Fim.')


    soma = barato = caro = menor = maior = quant = 0
while True:
    prod = str(input('Digite o produto: '))
    price = float(input('Digite o valor: R$'))
    cont = str(input('Quer continuar? [S/N] '))
    soma += price
    if cont in 'Ss':
        prod = str(input('Digite o produto: '))
        price = float(input('Digite o valor: R$'))
        cont = str(input('Quer continuar? [S/N] '))
        soma += price
        quant += 1
        if quant == 1 or price < barato:
            barato = price
            menor = prod
        elif quant == 1 or price > caro:
            caro = price
            maior = prod
    if cont in 'Nn':
        print(f'O valor total gasto foi de R${soma}.')
        print(f'O produto mais barato foi {menor}, com valor de R${barato}.')
        print(f'O produto mais caro foi {maior}, com valor de R${caro}.')
        break

else:
    print('Fim.')


--- caixa eletronico
valor = int(input('Valor do saque: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
            

TUPLAS-TUPLAS-TUPLAS-TUPLAS
São imutáveis.
print(sorted(nome_tupla))

lanche = ('Hamb', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont])

-resultado:
Hamb
Suco
Pizza
Pudim



for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

    
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(len(c))
resultado = 7

print(c.count(5))
resultado = 2

print(c.index(8))
resultado = 1 (2ª posição)

print(c.index(5, 1))
resultado = 5 (posição do num 5, a partir da segunda posição)


# tupla preenchida com contagem por extenso de 0 a 15. input numero, resultado por extenso

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze')
while True:
    num = int(input('Digite um número entre 0 e 15: '))
    if 0 <= num <= 15:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')




times = ('Cor', 'Pal', 'Sant', 'Grem', 'Cruze', 'Flam',
         'Vasco', 'Atlet', 'Corit', 'Ponte Preta', 'Sao Paulo',
         'Flumi', 'Atlet')

# for a in times:
#    print(a[0:5])

print(f'Lista de times: {times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os últimos são {times[-5:]}')
print(f'Times em ordem alf: {sorted(times)}')
print(f'O Vasco está na {times.index("Vasco")+1}ª posição.')



from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
soma = 0
mult = 1
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
    soma += n
    mult = mult * n
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
print(f'A soma foi de {soma}')
print(f'A mult foi de {mult}')





num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

        

# tupla com nome de produtos e preços

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Mochila', 80,
            'Canetas', 23.90)
print('-' * 38)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-' * 38)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-' * 38)


palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

"""

num = [2, 5, 9, 1]
# num[2] = 3
num.append(7)  # somente um número
# num.sort()
num.insert(2, 650)  # primeiro a posição em que vai ser inserido
num.sort(reverse=True)
num.insert(2, 0)  # a ordem importa
num.pop()  # remover último elemento. Entre () pode ser colocado a posição
num.remove(2)  # vai procurar o primeiro valor correspondente para eliminar
if 20 in num:
    num.remove(20)
print(num)
print(f'Essa lista tem {len(num)} elementos.')




valores = list()
valores.append(5)
valores.append(4)
valores.append(9)
valores.append(4)


for v in valores:
    print(f'{v} ', end='')

for c, b in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {b}.')



valores = list()
for cont in range(0, 6):
    valores.append(int(input('Digite um valor: ')))
print(valores)


a = [2, 3, 4, 7]
b = a[:]  # cria somente uma cópia, não uma ligação
b[2] = 8  # muda somente a lista b


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {valores}')
for c, b in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {b}.', end='')
print(f'O maior valor foi: {max(valores)}')
print(f'O menor valor foi: {min(valores)}')


valores = list()
mai = men = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {mai} nas posições ', end ='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i} ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i} ', end='')
print()


numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, não será adicionado.')
    r = str(input('Quer um continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(numeros)


a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = a[:]
b.sort(reverse=True)
print(b)


lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos+=1
print(f'Os valores digitados em ordem foram: {lista}')


valores = []
soma = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Valores em ordem decrescente {valores}')
if 5 in valores:
    print('Número 5 inserido na posição ', end='')
    for c, b in enumerate(valores):
        print(f'{c} ', end='')



expr = str(input('Digite sua expressão:'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válida.')
else:
    print('Inválida.')



galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'{totmai} maiores de idade e {totmen} menores de idade.')



lista = list()
dado = list()
maiorp = menorp = quant = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] '))
    quant += 1
    if resp in 'Nn':
        break
print(lista)
print(quant)







lista = list()
dado = list()
maiorp = menorp = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maiorp = menorp = dado[1]
    else:
        if dado[1] > maiorp:
            maiorp = dado[1]
        if dado[1] < menorp:
            menorp = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'O maior peso foi de {maiorp}Kgs de ', end='')
for p in lista:
    if p[1] == maiorp:
        print(f'{p[0]} ', end='')

print()
print(f'O menor peso foi de {menorp}Kgs de ', end='')
for p in lista:
    if p[1] == menorp:
        print(f'{p[0]} ', end='')
print(f'\nAo todo você cadastrou {len(lista)} pessoas.')


num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)


num[0].sort()
num[1].sort()
print(f'Todos os valores: {num}')
print(f'Pares: {num[0]}')
print(f'Impares: {num[1]}')





# matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  # para mudar a cada linha


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()  # para mudar a cada linha
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c]:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')


from random import randint
lista = list()
jogos = list()
print('-' * 30)
quant = int(input('Quantos jogos você quer fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')



ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 para finalizar): '))
    if opc == 000:
        print('Fim.')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')



