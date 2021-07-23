'''Crie um programa que leia nome,sexo e idade de várias pessoas em um dicionario{} e todos os dicionarios em uma lista[]
no final mostre.
a) quantas pessoas foram cad
b) a media de idade do grupo
c) uma lista com pessoas com idade acima da media'''

cadPessoa = {}
listaPessoa = list()
listaMulheres = list()
soma = 0
while True:
    cadPessoa['Nome'] = str(input('Nome: ')).capitalize()
    cadPessoa['Idade'] = int(input(f'Idade de {cadPessoa["Nome"]}: '))

    while True:
        cadPessoa['Sexo'] = str(input('Digite o Sexo [M/F]: ')).upper().strip()[0]
        if cadPessoa['Sexo'] in 'MF':
            break
        print('Opção Errada! Tente Novamente com [M/F]')

    listaPessoa.append(cadPessoa.copy())
    soma += cadPessoa['Idade']

    if cadPessoa['Sexo'] == 'F':
        listaMulheres.append(cadPessoa['Nome'])

    querContinuar = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]

    if querContinuar == 'N':
        break
        
print('=' * 25)
print(f'0 Grupo tem {len(listaPessoa)} Pessoas.')
print(f'Média de Idade: {soma / len(listaPessoa):.2f}')
print(f'Mulheres Cadastradas: {listaMulheres}')

for a in listaPessoa:
    if a['Idade'] >= soma / len(listaPessoa):
        print(f'{a["Nome"]}: {a["Idade"]}')
