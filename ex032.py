from datetime import date
ano = int(input('Se quiser analisar o ano atual digite 0 ou digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=o or ano % 400 == 0:
    print(f'O ano é {ano} BISSEXTO!')
else:
    print(f'O ano não é BISSEXTO!')

#Copiei porque não entendi.