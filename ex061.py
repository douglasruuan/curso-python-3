primeiroTermo = int(input('Digite o primeiro termo: '))
razaoPa = int(input('Digite a razao: '))
contador = 1

while contador <= 10:
    print(f'{primeiroTermo} → ',end='')
    primeiroTermo += razaoPa
    contador += 1
print('Fim')