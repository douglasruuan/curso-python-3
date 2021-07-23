"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionario com as seguintes informações.
Quantidade de notas
a maior nota
a menor nota
a média da turma
a situação opcional
adicione também as docstrings da função.

"""


def notas(*nota, situacao=False):
    """
      Função para receber notas e retornar um dicionário contendo informações sobre a turma
      :param nota: recebe as notas da turma.
      :return: retorna um dicionário contendo a quantidade de notas informadas, a maior e menor nota, além da média da turma.
      """
    infoAluno = dict()
    infoAluno['Quantidade de Notas'] = len(nota)
    infoAluno['Maior Nota'] = max(nota)
    infoAluno['Menor Nota'] = min(nota)
    infoAluno['Média Notas'] = sum(nota) / len(nota)
    if situacao:
        if sum(nota) / len(nota) >= 7:
            infoAluno['Situação da turma'] = 'Boa'
        elif sum(nota) / len(nota) >= 5:
            infoAluno['Situação da turma'] = 'Razoavel'
        else:
            infoAluno['Situação da turma'] = 'Ruim'

    for i, j in infoAluno.items():
        print(f'{i}: {j}')


# Programa Inicial
notas(3.5, 2, 6.5, 7, 10, 8, 2, situacao=False)
help(notas)
