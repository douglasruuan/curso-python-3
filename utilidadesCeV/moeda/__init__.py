import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def metade(p=0, formato=False):
    '''
    :param p: Recebe o valor do Input
    :param formato: Se True formata para R$ se false não.
    :return: Retorna o valor do input dividido / 2.
    '''

    novoPreco = p / 2
    return novoPreco if formato is False else moeda(novoPreco)


def dobro(p=0, formato=False):
    '''
    :param p: Recebe o valor do Input
    :param formato: Se True formata para R$ se false não.
    :return: Retorna o valor do input vezes * 2.
    '''

    novoPreco = p * 2
    return novoPreco if formato is False else moeda(novoPreco)


def aumentar(p=0, acrescimo=0, formato=False):
    '''
    :param p: Recebe o valor do Input
    :param acrescimo: Recebe o valor do acrescimo %.
    :param formato: Se True formata para R$ se false não.
    :return: Retorna o novo preço com acrescimo.
    '''

    novoPreco = p + (p * acrescimo / 100)
    return novoPreco if formato is False else moeda(novoPreco)


def diminuir(p=0, desconto=0, formato=False):
    '''
    :param p: Recebe o valor do Input
    :param desconto: Recebe o valor do desconto %.
    :param formato: Se True formata para R$ se false não.
    :return: Retorna o novo preço com desconto.
    '''
    novoPreco = p - (p * desconto / 100)
    return novoPreco if formato is False else moeda(novoPreco)


def moeda(p):
    '''

    :param p: Recebe o valor para conversão
    :return: retorna o valor utilizando currency convertido para R$.
    '''
    return locale.currency(p)


def resumo(preco, aumento, desconto):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado: ":<20}{moeda(preco):>10}')
    print(f'{"Dobro do preço: ":<20}{moeda(dobro(preco)):>10}')
    print(f'{"Metade do preço: ":<20}{moeda(metade(preco)):>10}')
    print(f'{aumento}{"% de aumento: ":<18}{moeda(aumentar(preco, aumento)):>10}')
    print(f'{desconto}{"% de desconto: ":<18}{moeda(diminuir(preco, desconto)):>10}')
