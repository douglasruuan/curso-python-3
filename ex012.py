p = input('Digite o Nome do Produto: ')
v = float(input('Digite o Preço deste Produto: '))
s = v - (v * 5 / 100)
print(f'O Preço do seu Produto é {v}\n'
      f'O Preço com Desconto é {s}')