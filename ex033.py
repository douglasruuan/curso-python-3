a = int(input('Digite o Primeiro Número: '))
b = int(input('Digite o Segundo Número: '))
c = int(input('Digite o Terceiro Número: '))
#Verificando o Menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando o Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O Menor Valor Digitado foi: {menor}\n'
      f'O Maior Valor Digitado foi: {maior}')