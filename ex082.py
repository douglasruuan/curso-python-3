'''Crie um programa que leia vários números e colocar em uma lista
depois crie 2 listas que vão contar apenas os valores pares e os valores impares digitados
no final mostre as 3 listas'''

lista = []
listapar = []
listaimpar = []

while True:
    addNumeros = int(input('Digite um número: '))
    lista.append(addNumeros)
    resto = addNumeros % 2

    if resto == 0:
        listapar.append(addNumeros)

    else:
        listaimpar.append(addNumeros)

    sair = str(input('Deseja Continuar?  [S/N]: ')).upper().strip()[0]

    if sair == 'N':
        break
print(f'Todos os Números: {lista}')
print(f'Todos Números Par: {listapar}')
print(f'Todos Números Impar: {listaimpar}')
