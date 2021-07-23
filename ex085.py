'''Crie um programa que o usuario possa digitar 7 valores numericos e cadastre em uma lista única
que mantenha os valores separados em pares e impares
no final mostre os valores pares e impares na ordem crescente.
'''

numero = [[], []]
for c in range(1, 8):
    numeros = int(input(f'Digite {c}º valor:  '))
    resto = numeros % 2
    if resto == 0:
        numero[0].append(numeros)
    else:
        numero[1].append(numeros)

numero[0].sort()
numero[1].sort()
print(f'Números pares em ordem crescente: {numero[0]}')
print(f'Números impares em ordem crescente: {numero[1]}')
