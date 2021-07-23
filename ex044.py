valorProduto = float(input('Digite o Valor das Compras: '))

print('1 - Para Avista Dinheiro.\n'
      '2 - Para Avista Cartão\n'
      '3 - Até 2x Cartão\n'
      '4 - Acima de 3x.')

formaPagamento = int(input('Digite a Forma de Pagamento: '))

if formaPagamento == 1:
    descDinheiro = valorProduto * 10 / 100
    valorDinheiro = valorProduto - descDinheiro
    print(f'Você irá ter 10% de Desconto.\n'
          f'Valor do Produto sem o desconto R${valorProduto}\n'
          f'Com Desconto ficará R${valorDinheiro}')
elif formaPagamento == 2:
    descCartao = valorProduto * 5 / 100
    valorCartao = valorProduto - descCartao
    print(f'Você irá ter 5% de Desconto.\n'
          f'Valor do Produto sem o desconto R${valorProduto}\n'
          f'Com Desconto ficará R${valorCartao}')
elif formaPagamento == 3:
    quantParc = valorProduto / 2
    print(f'Valor do Produto R${valorProduto} em 2x irá ficar sem JUROS.\n'
          f'Cada parcela sairá R$ {quantParc}')
elif formaPagamento == 4:
    quantParc = int(input('Digite Quantas parcelas acima de 3X você irá FAZER: '))
    cartaoJuros = valorProduto * 20 / 100
    valorJuros = valorProduto + cartaoJuros
    valorParcela = (valorJuros / quantParc)

    print(f'Você irá ter 20% de acréscimo acima de 2x... você parcelou em {quantParc}x.\n'
          f'Valor das compras R${valorProduto}\n'
          f'Com o acréscimo o valor ficará R${valorJuros}\n'
          f'Valor das parcelas em {quantParc}x irá ficar em R${valorParcela:.2f}')
else:
    print('DIGITE UMA OPÇÃO VÁLIDA, DE 1 A 4.')
