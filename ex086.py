'''Crie um programa que crie uma matriz de 3x3 e preencha com valores pelo teclado
no final mostre na tela com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
print('==' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
