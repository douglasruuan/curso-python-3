'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo numa lista.
no final mostre
a) quantas pessoas foram cadastradas
b) uma lista com as pessoas mais pesadas
c) uma lista com as mais leves
'''
principal = list()
temporario = list()
totalpessoas = 0
pesomaior = pesomenor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(int(input('Peso: ')))

    if len(principal) == 0:
        pesomaior = pesomenor = temporario[1]
    else:
        if temporario[1] > pesomaior:
            pesomaior = temporario[1]
        if temporario[1] < pesomenor:
            pesomenor = temporario[1]

    principal.append(temporario[:])
    temporario.clear()
    totalpessoas += 1

    desejaContinuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if desejaContinuar == 'N':
        break

print('=-' * 30)
print(f'Você Cadastrou, {totalpessoas} pessoas.')
print(f'O peso maior foi de {pesomaior}Kg.', end='')
for p in principal:
    if p[1] == pesomaior:
        print(f' [{p[0]}]')
print(f'O peso menor foi de {pesomenor}Kg.', end='')
for p in principal:
    if p[1] == pesomenor:
        print(f' [{p[0]}]')
