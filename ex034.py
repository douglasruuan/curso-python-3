nome = str(input('Digite seu Nome: '))
salario = float(input('Digite seu Sálario: '))
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Olá {nome}.\n'
          f'Seu Aumento de Salário de 10% ficou em R${aumento} mensais.')
else:
    aumento1 = salario + (salario * 15 / 100)
    print(f'Olá, {nome}\n'
          f'Seu Aumento de Salário de 15% ficou em R${aumento1} mensais.')