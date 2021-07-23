primeiroTermo = int(input('Digite o primeiro termo: '))
razaoPa = int(input('Digite a razao da PA: '))
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{primeiroTermo} → ', end='')
        primeiroTermo += razaoPa
        contador += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos deseja? '))
print('Fim')