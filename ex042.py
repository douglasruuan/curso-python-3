print('Digite 3 Segmentos para mim.')
r1 = float(input('Digite o Primeiro segmento: '))
r2 = float(input('Digite o Segundo segmento: '))
r3 = float(input('Digite o Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    if r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('NÃO PODEM FORMAR TRIÂNGULO.')