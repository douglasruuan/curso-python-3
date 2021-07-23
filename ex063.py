numeroTermo = int(input('Digite um termo: '))
pTermo = 0
sTermo = 1
contador = 3
print(f'{pTermo} → {sTermo} → ', end='')

while contador <= numeroTermo:
    tTermo = pTermo + sTermo
    print(f'{tTermo} → ', end='')
    pTermo = sTermo
    sTermo = tTermo
    contador += 1
print('FF')

