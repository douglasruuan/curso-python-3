def maior(*num):
    tam = len(num)
    maiorN = max(num)
    print('-=' * 30)
    print('Analisando os Valores')
    print(f'{num}  foram informados {tam} valores ao todo')
    print(f'O maior valor informado foi {maiorN}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
