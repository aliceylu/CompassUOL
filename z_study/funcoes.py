"""
Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada.

Exemplos:
print()
len()
max()
min()
count()
etc
"""

#print(type(nome_da_funcao()))
#Para descobrir o tipo da função.

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print ()

print(cores)

curso = 'Programação em Python: Essencial'

print (curso)

cores.append('roxo')

print (cores)

#curso.append('Mais dados...') - não é possivel usar append em strings

cores.clear()
# Irá limpar dados atribuídos de "cores"


"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde: 

nome_da_funcao -> SEMPRE com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos, que é 
utilizado em Python para definir blocos.

"""

# Definindo a primeira função:

def diz_oi():
    print('Oi!')

"""
OBS:
1 - Dentro das funções podemos utilizar outras funções;
2 - A função só executa 1 tarefa.
3 - A função não recebe nenhum parametro de entrada;
4 - A função não retorna nada.

O que não fazer ao definir funções:

diz_oi
diz_oi ()


"""

#Exemplo 2:

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('etc')

cantar_parabens()

for n in range(5):
    cantar_parabens()

# Repetir 5x. (0, 1, 2, 3, 4)

"""
Não muito utilizado, porém possível, podemos criar variáveis do tipo função
e executar esta função através da variável.

canta = cantar_parabens

canta()

O recomendado é que se necessário, seja renomeada a função original.

"""

#Funções com retorno

numeros = [1, 2, 3]

numeros.pop() # pop - Irá retirar o último número de uma lista.


numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')


#Exemplo função

def quadrado_de_7():
    print(7 * 7)

quadrado_de_7

#Resultado: imprimir 49
#Em Python, quando uma função não retorna nenhum valor, o retorno é None.

#Função com retorno de valor para refatorar/redefinir.

#Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
#Podemos passar a execução da função para outras funções.

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print(f'Retorno {ret}')

#ou
print(f'Retorno: {quadrado_de_7()}')
print(f'Retorno: {quadrado_de_7() + 1}')


#Refatorando primeira função

def diz_oi():
    return 'Oi! '

alguem = 'Nome'

print(diz_oi() + alguem)

#Não é possível somar None com string, por isso return deve ser usado.


"""
OBS: RETURN
1 - Ela FINALIZA a função, sai da execução da função;
2 - Podemos ter em uma função, diferentes returns porém só retorna 1.
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.
"""

#Exemplo:

def diz_oi():
    print('Linhas antes do return são executadas.')
    return 'Oi!'
    print('Linhas após return nunca são executadas.')



#Exemplo 2:

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b' #Não é necessário utilizar o "else"
    

print(nova_funcao())

#Dependendo do valor atribuído na variável, irá ignorar ou não os returns.
#Porém somente um valor será retornado.

#Exemplo 3:

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao() #desempacotar

print(num1, num2, num3, num4)

#Resultado: 2 3 4 5 

print(outra_funcao())
#Resultado em formato de tupla devido vírgulas: (2, 3, 4, 5)


#Criando função de cara ou coroa

from random import random

def joga_moeda():
    #Gera um número pseudo-randomico entre 0 e 1 (pode ter repetição de valores)
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

#Codificação desnecessária na utilização do retorno

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False
#desnecessário utilizar else

print(eh_impar())
