ano = int(input('Digite o seu Ano de nascimento: '))
idade = 2021 - ano
if idade < 18:
    a = 18 - idade
    print(f'Você tem {idade} anos.\n'
          f'Falta {a} anos para você se alistar.')
elif idade > 18:
    a = idade - 18
    print(f'Você tem {idade} anos.\n'
          f'Passou {a} anos do seu alistamento.')
