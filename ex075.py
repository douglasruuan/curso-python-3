num = (int(input('1º valor: ')), int(input('2º valor: ')), int(input('3º valor: ')), int(input('4º valor: ')))
print(num)
print(f'o Número 9 da tupla {num} apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'o número 3 apareceu na posição {num.index(3)}')
else:
    print('Não encontrado o número 3.')
print('Números pares digitados: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
