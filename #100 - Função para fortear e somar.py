#100 - Função para fortear e somar
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores de lista: ', end='')
    for cont in range(0,5):
        lista.append(randint(1,10))
    for e in lista:
        print(f'{e} ', end = '', flush = True)
        sleep(0.2)
def somapar(lista):
    s=0
    for e in lista:
        if e % 2 == 0:
            s += e
    print(f'\nSomando os valores pares de {lista}, temos {s}')

#programa principal
numeros = list()
sorteia(numeros)
somapar(numeros)
