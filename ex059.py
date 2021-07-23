digiteNumeroUm = int(input('Digite o primeiro valor: '))
digiteNumeroDois = int(input('Digite o segundo valor: '))
digiteUmNumeroMenu = 0

while digiteUmNumeroMenu != 5:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Números\n'
          '[5] Sair\n')
    digiteUmNumeroMenu = int(input('Digite número Menu: '))

    if digiteUmNumeroMenu == 1:
        soma = digiteNumeroUm + digiteNumeroDois
        print(f'A soma de {digiteNumeroUm} + {digiteNumeroDois} = {soma}')
    if digiteUmNumeroMenu == 2:
        soma = digiteNumeroUm * digiteNumeroDois
        print(f'A multiplicação de {digiteNumeroUm} * {digiteNumeroDois} = {soma}')
    if digiteUmNumeroMenu == 3:
        if digiteNumeroUm > digiteNumeroDois:
            print(f'O maior número digitado foi {digiteNumeroUm}')
        else:
            print(f'O maior número digitado foi {digiteNumeroDois}')
    if digiteUmNumeroMenu == 4:
        digiteNumeroUm = int(input('Digite o primeiro valor: '))
        digiteNumeroDois = int(input('Digite o segundo valor: '))
    if digiteUmNumeroMenu == 5:
        print('Você Escolheu sair do Programa.')

print('Sair Programa')
