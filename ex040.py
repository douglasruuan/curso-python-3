n1 = float(input('Digite sua N1: '))
n2 = float(input('Digite sua N2: '))

media = (n1 + n2) / 2

if media <= 5.0:
    print(f'Sua média foi {media} você está REPROVADO')
elif media >= 5.0 and media <= 7.0:
    print(f'Sua média está {media} você está em RECUPERAÇÃO')
elif media >= 7.0:
    print(f'Sua média foi {media} você foi APROVADO.')
