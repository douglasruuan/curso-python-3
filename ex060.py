numeroFatorial = int(input('Digite número para calcular seu Fatorial: '))
f = 1
print(f'Calculando {numeroFatorial}! = ', end='')
while numeroFatorial > 0:
    print(f'{numeroFatorial}',end='')
    print(f' x ' if numeroFatorial > 1 else ' = ', end='')
    f *= numeroFatorial
    numeroFatorial-= 1
print(f'{f}')

