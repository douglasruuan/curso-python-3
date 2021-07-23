qtd = soma = 0
while True:
    numeroUsuario = int(input('Digite um numero: '))
    if numeroUsuario == 999:
        break
    qtd += 1
    soma += numeroUsuario
print(f'Foi digitado {qtd} e a soma é {soma}')