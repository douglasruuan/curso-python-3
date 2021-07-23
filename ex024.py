nome = input('Digite o Nome da sua Cidade: ').strip().upper().split()
nome1 = 'SANTO' in nome[0]
print(f'Existe o nome Santo no inicio da sua Frase? {nome1}')