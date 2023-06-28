#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from time import sleep
print('-=-'*10)
print('     Analisador de ano     ')
print('-=-'*10)

ano = int(input('Informe um ano:'))
print('Processando...')
sleep(3)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

