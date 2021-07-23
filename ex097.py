'''Faça um programa que tenha uma função chamada escrever(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.'''


def escreva(msg):
    len(msg)
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


txt = str(input('Mensagem: '))

escreva(txt)
