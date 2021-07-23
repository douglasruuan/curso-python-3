valores = list()

for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'''\nMaior valor digitado: {max(valores)}
Posição: ''', end='')

for i in range(0, 5):

    if valores[i] == max(valores):
        print(i, end=' ')

print(f'''\n \nMenor Valor digitado: {min(valores)}
Posição: ''', end='')

for i in range(0, 5):
    if valores[i] == min(valores):
        print(i, end=' ')
