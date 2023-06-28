#escreva um progra que faça o computador pensar em um numero entre zero e 5 o usuario tenta advinhar e se acertar devera escrever venceu ou perdeu
from random import randint
from time import sleep
num = randint(0,5)
print('-=-'*20)
print('O computador escolheu um numero de 0 a 5, tente advinhar!')
print('-=-'*20)
n = int(input('Digite um número: '))
print('Processando...')
sleep(3)
if n == num:
    print('Você Ganhou!!!')
else:
    print("Você perdeu :(")