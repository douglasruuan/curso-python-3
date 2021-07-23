jogador = {}
gols = list()
jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))

if partidas > 0:

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}º partida? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

print('=-' * 24)

print(jogador)

print('=-' * 24)
for k, v in jogador.items():
    print(f'{k}: {v}')

print('=-' * 24)

print(f'O Jogador {jogador["Nome"]} jogou {partidas} partida.')

for i, j in enumerate(gols):
    print(f'   => Na Partida {i + 1} fez {j} gols. ')

print(f'Foi um total de {jogador["Total"]} de gols.')
