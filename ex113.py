"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido Aproveite e cria também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDigite Inteiro Válido.\033[m')
        except KeyboardInterrupt:
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDigite Real Válido.\033[m')
        except KeyboardInterrupt:
            return 0
        else:
            return f


num1 = leiaInt('Inteiro: ')
num2 = leiaFloat('Real: ')

print('-' * 30)
print(f'Número Inteiro {num1}')
print(f'Número Real {num2}')
