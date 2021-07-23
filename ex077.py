palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'

for palavra in palavras:
    print(f'\nPara Palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')
