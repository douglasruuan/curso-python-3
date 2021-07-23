"""
Exercício Python 103 - Ficha do Jogador
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado
"""


def ficha(nome='desconhecido', gol=0):
    print('--' * len(n + nome))
    print(f'Nome do Jogador: {nome}\n'
          f'Quantidade de Gols: {gol}')


n = str(input('Nome Jogador: '))
g = str(input('Gols Jogador: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
