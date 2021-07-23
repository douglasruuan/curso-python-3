numeros = list()
cont = 0

while True:
    addNumeros = int(input('Digite um número: '))
    sair = str(input('Deseja Continuar?  [S/N]: ')).upper().strip()[0]
    if sair == 'N':
        numeros.append(addNumeros)
        cont += 1
        break
    if addNumeros not in numeros:
        numeros.append(addNumeros)
        cont += 1

numeros.sort(reverse=True)

print('=-=' * 20)
print(f'Quantidade de Elementos: {cont}')
print(f'Lista em Ordem Decrescente: {numeros}')
if 5 in numeros:
    print('Numero está 5 na lista.')
else:
    print('O Numero 5 não está na Lista.')
