resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um numero: '))
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    soma = soma + num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f'Você digitou {quant} de numeros.\n'
      f'Sua media ficou {media}\n'
      f'O maior numero {maior}\n'
      f'O menor numero {menor}')