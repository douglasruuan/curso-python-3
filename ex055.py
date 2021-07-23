pesoMaior = 0
pesoMenor = 0

for p in range (1, 6):
    peso = float(input(f'Peso da {p}º Pessoa: '))
    if p == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'O Maior peso Lido {pesoMaior}Kg')
print(f'O Menor peso Lido {pesoMenor}Kg')