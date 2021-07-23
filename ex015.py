km = float(input('Digite Quantos KM você Utilizou? '))
dias = int(input('Digite Quantos Dias você ficou com o Carro? '))
s = (dias * 60) + (km * 0.15)
print(f'Você Utilizou o Carro por {dias} Dias.\n'
      f'Você Rodou a Quantidade de {km} Kilometros.\n'
      f'O Total para você pagar é de ${s:.2f} Reais.')
