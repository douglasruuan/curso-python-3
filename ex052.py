n1 = int(input('Digite um número: '))
tot = 0
for c in range (1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\nO Número {n1} foi divisível {tot} vezes.')
if tot == 2:
    print('Ele é PRIMO')
else:
    print('Ele não é PRIMO.')