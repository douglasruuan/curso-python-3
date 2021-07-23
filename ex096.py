'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular, ( largura e comprimento)
e mostre a area do terreno.'''


def area(largura, comprimento):
    total = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {total}m²')


print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Área do Terreno: '))
comprimento = float(input('Comprimento do Terreno: '))

area(largura, comprimento)
