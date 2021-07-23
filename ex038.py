n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite Outro Número: '))

if n1 > n2:
    print(f'{n1} é maior que o Número {n2}.')
elif n2 > n1:
    print(f'{n2} é maior que o Número {n1} ')
elif n2 == n1:
    print(f'Os números {n1} e {n2} são iguais.')
