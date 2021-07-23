import random
print(' → Vamos Jogar Par ou Imar! ← ')
vitoria = 0
while True:
    numerousuario = int(input('Digite um Número: '))
    computadorRandomico = random.randint(0,10)
    total = numerousuario + computadorRandomico
    tipoParImpar = ' '
    while tipoParImpar not in 'PI':
        tipoParImpar =str(input('Par ou Impar?[P/I]: ')).upper().strip()[0]
    print(f'Você jogou {numerousuario} e o Computador {computadorRandomico}. Total de {total}')
    if tipoParImpar == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria+= 1
        else:
            print('Você PERDEU!')
            break
    elif tipoParImpar == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')

