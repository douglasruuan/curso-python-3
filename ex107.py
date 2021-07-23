"""
crie um modulo chamado moeda.py que tenha as funções incorporadas
aumentar(),diminuir(),dobro(),metade().
faça também um programa que importe esses módulo e use algumas dessas funções.
"""

from utilidadesCeV import moeda

p = float(input('Preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p, 10)} ')
print(f'Descontando 13% de {p}, temos {moeda.diminuir(p, 13)}')
