nome = str(input('Digite seu Nome: ')).title()
peso = float(input('Digite seu Peso (kg): '))
altura = float(input('Digite sua Altura (m): '))
imc = peso / (altura ** 2)

print(f'O seu imc é de {imc:.2f}')

if imc < 18.5:
    print(f'Olá {nome}, você está abaixo do Peso.')
elif 18.5 <= imc < 25:
    print(f'Olá {nome}, você está no peso Ideal.')
elif 25 <= imc < 30:
    print(f'Olá {nome}, você está SobrePeso')
elif 30 <= imc < 40:
    print(f'Olá {nome}, você está com obesidade')
elif imc > 40:
    print(f'Olá {nome}, você está com Obesidade VAI MORRE CPX.')
