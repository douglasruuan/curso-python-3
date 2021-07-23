"""
Crie um Pequeno Sistema modularizado
que permita cadastrar pessoas pelo seu nome e idade em um arquivo.txt
o Sistema só vai ter 2 Opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
import os
import funcoesEx115

layout = {'limpar': '\033[m',
          'azul': '\033[36m',
          'amarelo': '\033[33m',
          'vermelho': '\033[31m',
          'barra': '----------------------------------------'}


while True:
    print(layout['azul'])
    print(layout['barra'])
    print('SISTEMA DE CADASTRO DE PESSOAS'.center(40))
    print(layout['barra'])
    print('''     1 - Ver Pessoas Cadastradas\n     2 - Cadastrar nova Pessoa\n     3 - SAIR''')


    op = int(input('\033[1;33mSua Opção: '))

    if op == 1:
        print(layout['amarelo'])
        print(layout['barra'])
        print('PESSOAS CADASTRADAS'.center(40))
        print(layout['barra'])
        funcoesEx115.imprimir()
        print(layout['barra'], layout['limpar'])
        os.system("PAUSE")

    elif op == 2:

        print(layout['amarelo'])
        print(layout['barra'])
        print('NOVO CADASTRO'.center(40))
        print(layout['barra'])

        nome = input('Informe o Nome: ')
        idade = int(input('Informe a Idade: '))

        funcoesEx115.cadastrarPessoa(nome, idade)
    elif op == 3:
        print(layout['amarelo'])
        print('Volte Sempre!')
        print(layout['limpar'])
        break

    else:
        print(layout['vermelho'])
        print('Opção inválida!')
        print(layout['limpar'])
        os.system("PAUSE")