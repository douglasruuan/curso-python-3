soma = 0
for c in range (1,6+1):
    num = int(input(f'Digite o Número {c}: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A Soma de todos os Números Pares são: {soma}.')