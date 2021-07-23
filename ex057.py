sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo, corretamente [M/F]: ')).upper().strip()[0]
print('Sexo Cadastrado.')