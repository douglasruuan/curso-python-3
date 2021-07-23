import random
print('→ Jogo da Adivinhação ←')
computadorRandomico = random.randint(0,11)
print(computadorRandomico)
usuarioNumero = int(input('Digite um número: '))
quantidadeUsuario = 1

while computadorRandomico != usuarioNumero:
    usuarioNumero = int(input('Digite novamente até acertar: '))
    quantidadeUsuario += 1
print(f'Você acertou e tentou {quantidadeUsuario} vezes. ')
