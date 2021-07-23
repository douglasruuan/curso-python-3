frase = str(input('Digite uma Frase: ')).upper()
letra = frase.count('A')
print(f'A letra A aparece: {letra} vezes.\n'
      f'A letra A apareceu na posição: {frase.find("A")+1}\n'
      f'A última letra A apareceu na posição: {frase.rfind("A")+1}')