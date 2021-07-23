frase = str(input('Digite uma Frase para Verificar se ela é Palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
if inverso == junto:
    print('Temos um Palindromo.')
else:
    print('Não é Palindromo.')
print(inverso)