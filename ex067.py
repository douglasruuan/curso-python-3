while True:
    num = int(input('Digite um numero para tabuada: '))
    if num <= 0:
        print('Número Negativo')
        break
    for c in range(1, 10 + 1):
        print(f'{num} x {c} = {num * c}')
print('Fim')


