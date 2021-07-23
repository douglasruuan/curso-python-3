"""
Exercício Python 111 - Transformando módulos em pacotes
Dentro do pacote que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from utilidadesCeV import dados, moeda

p = dados.leiaDinheiro('Digite o Preço: R$ ')
moeda.resumo(p, 35, 22)
