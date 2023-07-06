#99 - Função que descobre o maior
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i} ', end = '', flush = True)
        sleep(0.2)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()