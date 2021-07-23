num = int(input('Digite um Número: '))

print(' 1 - Binario\n'
      ' 2 - Octal\n'
      ' 3 - Hexadecimal\n'
      ' 4 - Para Todos')
base = int(input('Digite a Base de Conversão: '))

if base == 1:
    numero = bin(num)
    print(f'{numero}')
elif base == 2:
    numero = oct(num)
    print(f'{numero}')
elif base == 3:
    numero = hex(num)
    print(f'{numero}')
elif base == 4:
    numero = bin(num),oct(num),hex(num)
    print(f'{numero}')

else:
    print('Você nao digitou nada.')