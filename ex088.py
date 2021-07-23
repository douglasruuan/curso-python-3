#   Exercício Python 088 - Palpites para a Mega Sena
#   Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#   O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo.

import numpy as np

quantosjogos = int(input('Quantos Jogos Você Deseja?: '))

for l in range(1, quantosjogos + 1):
    megasena = np.random.randint(1, 60, (quantosjogos, 6))
print('Jogos Megana Sena da Semana ')
print(megasena)
