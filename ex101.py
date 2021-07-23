""" Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando
 um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições."""
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()


def opcaoVoto(ano):
    idade = date.year - ano
    if idade > 65:
        print(f'Sua idade {idade}: VOTO OPCIONAL.')
    elif idade > 18:
        print(f'Sua idade {idade}: VOTO OBRIGATÓRIO.')
    elif idade < 18:
        print(f'Sua idade {idade}: NÃO VOTA!')
    return ano


print('--' * 20)
anoNascimento = int(input('Ano de Nascimento: '))
opcaoVoto(anoNascimento)
