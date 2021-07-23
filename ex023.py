num = int(input('Digite um Número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando seu Número: {num}\n'
      f'Unidade: {u}.\n'
      f'Dezena: {d}.\n'
      f'Cetena: {c}.\n'
      f'Milhar: {m}.\n')
