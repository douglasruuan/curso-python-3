print('=='*18)
print('| Aprovação de Empréstimo Bancário.|')
print('=='*18)

nome = str(input('Digite seu Nome: '))
print(f'Obrigado Sr(a) {nome}.\n')

valorCasa = float(input(f'Digite por gentileza, Sr(a) {nome}.\n'
                        f' o Valor da Casa R$   '))
salario = float(input(f'Digite por gentileza, Sr(a){nome}\n'
                      f' Digite seu Sálario R$ '))
ano = float(input('Para finalizarmos.\n'
                            'Quantos anos de financiamento?: '))

calcValor = valorCasa / (ano * 12)
minimo = salario * 30 / 100

if calcValor <= minimo:
    print(f'Sr(a) {nome}, Conseguiu o Empréstimo Parabéns. ')
else:
    print(f'Infelizmente Sr(a) {nome}, não poderemos fazer o empréstimo.')


print(f'Sua Renda de R${salario}.\n'
      f'Valor da Casa divido com os Meses: R${calcValor:.2f}\n'
      f'Sobraria pro, Sr(a) R${salario-calcValor:.2f}')
