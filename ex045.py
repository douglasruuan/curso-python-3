import random
from time import sleep
print('==' * 12)
print('| Vamos Jogar Jokenpô? |')
print('==' * 12)

print('Sendo.')
print('0 - Pedra \n'
      '1 - Papel\n'
      '2 - Tesoura')
ppt = int(input('Digite sua Jogada: '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('POOOOO!!!!!!')

itens = ('Pedra','Papel','Tesoura')
pc = random.randint(0,2)
print('==' * 12)
print('| Analisando....Jokenpô? |')

if pc == ppt:
    print(f'EMPATE\n'
          f'Ambos escolheram {itens[pc]}')

elif ppt == 0 and pc == 2:
    print(f'Você escolheu {itens[ppt]}.\n'
          f'Computador escolheu {itens[pc]}\n'
          f'VOCÊ GANHOU!')
elif ppt == 0 and pc == 1:
    print(f'Você escolheu {itens[ppt]}\n'
          f'Computador escolheu {itens[pc]}\n'
          'VOCÊ PERDEU!')
elif ppt == 1 and pc == 0:
    print(f'Você escolheu {itens[ppt]}\n'
          f'Computador escolheu {itens[pc]}\n'
          'VOCÊ GANHOU!')
elif ppt == 1 and pc == 2:
    print(f'Você escolheu {itens[ppt]}\n'
          f'Computador escolheu {itens[pc]}\n'
          'VOCÊ PERDEU!')
elif ppt == 2 and pc == 1:
    print(f'Você escolheu {itens[ppt]}\n'
          f'Computador escolheu {itens[pc]}\n'          
          'VOCÊ GANHOU!')
elif ppt == 2 and pc == 0:
    print(f'Você escolheu {itens[ppt]}\n'
          f'Computador {itens[pc]}\n'
          'VOCÊ PERDEU!')
else:
    print('DIGITE DE UM 0 A 2....')

print('==' * 12)