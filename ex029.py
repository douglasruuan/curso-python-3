import random
vCarro = random.randint(40,100)
multa = vCarro - 80
pMulta = (multa * 7)

if vCarro <= 80:
    print(f'Você não foi Multado, você passou a {vCarro}')
else:
    print(f'Você foi Multado sua velocidade foi {vCarro}\n'
          f'Você vai ter que pagar {pMulta} Reais de Multa.')
