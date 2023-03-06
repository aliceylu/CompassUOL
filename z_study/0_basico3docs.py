def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)





def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} o voto é opcional.'
    else:
        return f'Com {idade} anos o voto é obrigatório.'


nasc = int(input('Digite o ano de nascimento. '))
print(voto(nasc))





def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))








def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show:  (opcional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5))
print(fatorial(5, show=True))
help(fatorial)




def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)



def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro. Digite um número inteiro válido.')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')




def notas(*n, sit=False):
    """
    -> Função para anlisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)





def ajuda(com):
    help(com)


comando = ''
while True:
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)





class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Andar(self):
        print('Andar')

    def Parar(self):
        print('Parar')

    def ExibirInfo(self):
        print(self.marca, self.modelo, self.ano)

carro1 = Carro('Peugeot', '208', '2007')
carro1.Andar()
carro1.Parar()
carro1.ExibirInfo()





class DidaticaTech:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print('Ultrapassou 12')
        else:
            print('Não ultrapassou 12')
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)




## split
frutas_lista = frutas_usuario.split(', ')

cores = ['a', 'b', 'c']
valores = ['1', '2', '3']

duas_listas = zip(cores, valores)