print('=' * 40)
timesBrasileirao = 'Athletico-PR', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Atletico-MG', 'Fluminense', 'Bahia', 'Aletico-GO', 'Santos', 'Flamengo', 'Corinthians', 'Ceara-SC', 'Internacional', 'Juventude', 'Sport-Recife', 'Chapecoense', 'Cuiaba', 'Sao Paulo', 'America-MG', 'Gremio'

print(f'Times do Brasileirao 2021 {timesBrasileirao}')
print('=' * 40)
print(f'Os Cincos Primeiros {timesBrasileirao[0:5]}')
print('=' * 40)
print(f'Os Quatros Ultimos {timesBrasileirao[-4:]}')
print('=' * 40)
print(f'Time em Ordem Alfabetica {sorted(timesBrasileirao)}')
print('=' * 40)
print(f'A Chape está na {timesBrasileirao.index("Chapecoense") + 1}º posição.')
