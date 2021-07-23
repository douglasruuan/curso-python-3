'''Aprimore o desafio
a) a soma de todos os números pares
b) a soma dos valores da terceira coluna
c) a soma dos valores da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somaterceira = 0
maiorvalor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))

print('==' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        resto = matriz[l][c] % 2
        if resto == 0:
            soma += matriz[l][c]
    print()
print('==' * 30)
print(f'A soma dos valores pares é: {soma}')
for l in range(0, 3):
    somaterceira += matriz[l][2]
print(f'A soma da Terceira coluna é: {somaterceira}')
for l in range(0, 3):
    if l == 0:
        maiorvalor = matriz[1][c]
    elif matriz[1][c] > maiorvalor:
        maiorvalor = matriz[1][c]
print(f'O Maior valor da segunda linha é: {maiorvalor}')
