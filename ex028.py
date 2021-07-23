import random
numRandom = random.randint(1,5)
numUsu = int(input('Digite um Número de 1 a 5: '))

if numUsu == numRandom:
    print(f'Parabéns você acertou o Número {numRandom}')
else:
    print(f'Você errou o número foi {numRandom}')