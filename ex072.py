contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinto', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove',
            'Vinte')
usuarioDigita = int(input('Digite um Número: '))
while usuarioDigita not in range(0, 21):
    print('Erro.')
    usuarioDigita = int(input('Digite um número de 0 a 20:'))

print(f'Você digitou o número {contagem[usuarioDigita]}')
