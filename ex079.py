numeros = list()
while True:
    addNumeros = int(input('Digite um número: '))
    sair = str(input('Deseja Continuar?  [S/N]: ')).upper().strip()[0]
    if sair == 'N':
        numeros.append(addNumeros)
        break
    if addNumeros not in numeros:
        numeros.append(addNumeros)
    else:
        print('Número Duplicado')
numeros.sort()
print(f'Valores Digitados: {numeros}')
