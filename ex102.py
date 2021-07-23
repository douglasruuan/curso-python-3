"""   Exercício Python 102 - Função para Fatorial
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial. """


def fatorial(num=1, show=False):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    if show:
        for i in range(num, 0, -1):
            if i == 1:
                print('2', end='')
            else:
                print(i, end=' x ')
        print(f' = {fat}')
    else:
        print(f'Fatorial de {num}! é {fat}')


n = int(input('Número: '))
mostrar = int(input('Mostrar tela? [0-não/1-sim]: '))
fatorial(n, mostrar)
