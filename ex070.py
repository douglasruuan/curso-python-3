totalGasto = 0
qtdProd = 0
precoMenor = 0
contador = 0
produtoBarato = ''
while True:
    nomeProduto = str(input('Digite nome do produto: '))
    precoProduto = float(input('Preço: R$ '))
    contador += 1
    totalGasto += precoProduto

    if precoProduto >= 1000:
        qtdProd += 1
    if contador == 1 or precoProduto < precoMenor:
        precoMenor = precoProduto
        produtoBarato = nomeProduto

    desejaContinuar = ' '
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if desejaContinuar == 'N':
        break
print(f'O preço total das compras foi de: R${totalGasto:.2f}\n'
      f'Quantidade de produtos acima de R$1000,00 são de: {qtdProd}\n'
      f'Menor Preço digitado e de R${precoMenor:.2f}\n'
      f'E o nome do Produto mais barato é: {produtoBarato}')
