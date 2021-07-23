from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} passo {p}')
    for n in range(i, f, p):
        print(f'{n} ', end='')
        sleep(0.2)
    print('Fim')


contador(0, 11, 1)
contador(10, -1, -1)

print('Personalize a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
