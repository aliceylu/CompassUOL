filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values())  # Star Wars, 1977, George Lucas
print(filme.keys())  # titulo, ano, diretor
print(filme.items())  # tudo

for k, v in filme.items():
    print(f'O {k} é {v}')
    

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())  # nome, sexo, idade
print(pessoas.items())  # [('nome', 'gustavo'), ('sexo', 'm'), ('idade', '22')]
pessoas['nome'] = 'Leandro'  # substituir Gustavo
pessoas['peso'] = 98.5  # adicionar key + valor




brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # não pode ser usado [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')


## exercícios

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' {k}: {v}')

## ou
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')



from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}.')



from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: (0 se não houver) '))
if dados['ctps'] != 0:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: R$ '))
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
        print(f'- {k} tem o valor {v}')



jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
        print(f'Na partida {i}, fez {v} gols.')
print(f'Total de {jogador["total"]} gols.')



galera = list()
pessoa = dict()  # temporário
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro. Valores aceitados somente M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro. Valores aceitos somente S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()

print('Fim.')




time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro. Apenas S ou N.')
    if resp == 'N':
        break
## resultados
print('-' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com o código {busca}.')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}: ')  # puxar nome correspondente
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 30)


## funções

def area(a, b):
    mult = a * b
    print(f'Área total do terreno com {a:.2f} x {b:.2f} de {mult} m²')


print('Controle de área')
print('-' * 20)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)



def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Mensagem aqui')







from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista....')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)






from time import sleep


def contador(i, f, p):
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim.')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim.')





contador(1, 10, 1)
contador(2, 38, 3)
print('-' * 20)
print('Escolha os valores:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)







def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados.....')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 5, 8, 7, 6, 0, 3)






