aluno = {}
aluno['nome'] = str(input('Digite Nome: ')).capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno["media"] >= 6:
    aluno['situacao'] = 'Aprovado'
    print(f'Nome é igual {aluno["nome"]}\n'
          f'Média é igual a {aluno["media"]}\n'
          f'Você está {aluno["situacao"]}')
else:
    aluno['situacao'] = 'Reprovado'
    print(f'Nome é igual {aluno["nome"]}\n'
          f'Média é igual a {aluno["media"]}\n'
          f'Você está {aluno["situacao"]}')

print(aluno)
