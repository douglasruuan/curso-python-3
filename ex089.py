'''Crie um programa que leia o nome e duas notas de vários alunos guarde tudo em uma lista composta no final mostre
boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
'''

lista = list()
while True:
    n = str(input('Digite seu Nome: ')).capitalize()
    n1 = float(input('Digite sua N1: '))
    n2 = float(input('Digite sua N2: '))
    media = (n1 + n2) / 2
    lista.append([n, [n1, n2], media])
    desejaContinuar = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    if desejaContinuar == 'N':
        break
print('=-' * 30)
print(f'{"Nº":<5}{"NOME":^10}{"MÉDIA":^20}')
print('=-' * 30)
for n, l in enumerate(lista):
    print(f'{n:<5} | {l[0][:]:<10} | {l[2]:>5} |')
print('=-' * 30)
while True:
    notaAluno = int(input('Deseja A Nota de Algum Aluno? (999 Pausa): '))
    if notaAluno == 999:
        print('Programa Pausado Até Logo.')
        break
    for n, l in enumerate(lista):
        if notaAluno == n:
            print(f'Notas de {l[0]:} é {l[1]:}')
