primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

dec = primeiro + ( 10 - 1 ) * razao
print(dec)
for c in range(primeiro, dec + razao, razao):
    print(f'{c}', end='> ')
print('ACABOUUUU.')