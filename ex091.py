'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios ( 1 e 6 ).
guarde esses resultados aleatorios em um dicionario.
No final coloque esse dicionario em ordem sabendo que o vencedor tirou o maior numero do dado'''
from time import sleep
from random import randint
from operator import itemgetter

jogadores = {
    '1º Jogador:': randint(1, 6),
    '2º Jogador:': randint(1, 6),
    '3º Jogador:': randint(1, 6),
    '4º Jogador:': randint(1, 6)
}
ranking = list()
print('Jogo de Dados ....')
print('==' * 30)
for k, v in jogadores.items():
    print(f'{k} Tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('==' * 30)
print('=== Ranking Jogadores ===')
for i, v in enumerate(ranking):
    print(f' {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
