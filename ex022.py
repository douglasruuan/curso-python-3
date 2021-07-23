nome = input('Digite seu Nome Completo: ').strip()
maiFrase = nome.upper()
minFrase = nome.lower()
divido = nome.split()
nome2 = "".join(divido)

print(f'Seu Nome é: {nome}\n'
      f'Seu Nome Maiuscúlo é: {maiFrase}\n'
      f'Seu Nome Minuscúlo é: {minFrase}\n'
      f'Quantidade de Caracteres: {len(nome2)}\n'
      f'Seu primeiro nome tem: {len(divido[0])}')