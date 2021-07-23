kmDistancia = int(input('Digite a Distancia da sua Viagem: '))
if kmDistancia >= 200:
    precoLonge = (kmDistancia * 0.45)
    print(f'Sua viagem vai custar R${precoLonge:.2f} Reais.')
else:
    precoPerto = (kmDistancia * 0.50)
    print(f'Sua viagem vai custar R${precoPerto:.2f} Reais.')