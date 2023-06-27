#jogo do acerto o numero 

from random import randint
from time import sleep
num = randint(0,10)
print('-=-'*20)
print('O computador escolheu um numero de 0 a 10, tente advinhar!')
print('-=-'*20)
count = 1
n = 0
while n != num:
    n = int(input('Digite um número: '))
    print('Processando...')
    sleep(.5)
    if n == num:
        print('Você Ganhou!!!')
    elif n < num:
        print("Mais...Tente outra vez")
        count += 1
    elif n > num:
        print('Menos...Tente outra vez')
        count += 1
print('Parabens, você acertou com {} tentativas'.format(count))
