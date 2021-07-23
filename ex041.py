nome = str(input('Digite seu Nome: '))
ano = int(input('Digite seu Ano de Nascimento: '))
idade = 2021 - ano

if idade <= 9:
    print(f'{nome}, você tem {idade} e está na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print(f'{nome}, você tem {idade} e está na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print(f'{nome}, você tem {idade} e está na categoria Junior.')
elif idade == 20:
    print(f'{nome}, você tem {idade} e está na categoria Sênior.')
elif idade > 20:
    print(f'{nome}, você tem {idade} e está na categoria Master')