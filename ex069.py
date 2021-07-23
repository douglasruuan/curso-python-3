print('==' * 13)
print('| Cadastro Idade / Sexo. |')
print('==' * 13)

idadeMaior = 0
totalHomem = 0
totalM20 = 0
while True:
    idadePessoa = int(input('Digite Idade: '))
    sexoPessoa = ' '
    while sexoPessoa not in 'MF':
        sexoPessoa = str(input('Digite Sexo [M/F]: ')).strip().upper()[0]
    if idadePessoa >= 18:
        idadeMaior += 1
    if sexoPessoa == 'M':
        totalHomem += 1
    if sexoPessoa == 'F' and idadePessoa < 20:
        totalM20 += 1

    desejaContinuar = ' '
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if desejaContinuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {idadeMaior}.\n'
      f'Total de Homens cadastrados é: {totalHomem}.\n'
      f'Total de Mulheres com menos de 20 anos: {totalM20}.\n')
