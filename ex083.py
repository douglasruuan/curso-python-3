'''Crie um programa que o usuario digite uma expressão qualquer que use
parenteses. Seu programa deverá analisar se a expressao passada esta com os paretenses abertos e fechados na ordem correta.'''

expressao = str(input('Digite uma expressão: '))
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Expressão Errada.')
