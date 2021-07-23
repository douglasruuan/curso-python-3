import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = math.hypot(co,ca)
print(f'A Hipotenusa Vai Medir {hi:.2f}')