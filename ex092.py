'''crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre os com idade em um dicionario.
se por acaso a CTPS for diferente de 0, o dicionario recebera tambem o ano de contratação e o salario.
calcule e acrecente alem da idade com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

cadPessoa = {}
while True:
    cadPessoa['nome'] = str(input('Seu Nome: ')).capitalize()

    nascimento = int(input('Ano de Nascimento: '))
    cadPessoa['idade'] = datetime.now().year - nascimento

    cadPessoa['CTPS'] = int(input('Carteira de Trabalho, [0 não tem]:  '))

    if cadPessoa['CTPS'] == 0:
        print(cadPessoa)
        for v, k in cadPessoa.items():
            print(f'{v}: {k}.')
        break

    cadPessoa['anoContrato'] = int(input('Ano de Contratação: '))

    if cadPessoa['anoContrato'] != 0:
        atual = cadPessoa['anoContrato'] - nascimento + 35
        cadPessoa['aposentadoria'] = atual

    cadPessoa['salario'] = float(input('Salário R$: '))

    print('== Informando Dados ==')
    print(cadPessoa)
    for v, k in cadPessoa.items():
        print(f'{v}: {k}.')
    break
