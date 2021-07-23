'''Aprimore o desafio 93 para que ele funcione com varios jogadores incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''
jogador = {}
gols = list()
time = list()
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))

    if partidas > 0:

        for c in range(0, partidas):
            gols.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}º partida? ')))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        desejaContinuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if desejaContinuar in 'SN':
            jogador.clear()
            gols.clear()
            break
        print('Opção inválida! Tente novamente.')
    if desejaContinuar == 'N':
        break

print('-=' * 20)

print(f'{"Cod":<5}{"NOME":<10}{"Total":<10}{"Gols":<10}')
for i, j in enumerate(time):
    print(f'{i:<5}{j["Nome"]:<10}{j["Total"]:<10}{j["Gols"]}')

print('-=' * 20)

while True:
    aux = int(input('Mostrar os dados de qual jogador? (999 sair) '))
    if aux == 999:
        break
    else:
        print(f'--- LEVANTAMENDO DO JOGADOR {time[aux]["Nome"]}')
        for i, j in enumerate(time[aux]["Gols"]):
            print(f'     Na {i + 1}º partida fez {j} gol(s)')
