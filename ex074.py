from random import sample

numeroAleatorio = tuple(sample(range(10), 5))
print(f'Os números sorteados são:')
for i in numeroAleatorio:
    print(f'{i}', end=' ')
print(f'\nMaior Número: {max(numeroAleatorio)}\n'
      f'Menor Número: {min(numeroAleatorio)}')
