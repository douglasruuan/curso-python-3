soma = 0
cont = 0
for num in range (1,501, 2):
    if num % 3 == 0:
        soma = soma + num
        cont += 1
print(f'A soma de todos os Números é de: {soma}\n'
      f'{cont}')