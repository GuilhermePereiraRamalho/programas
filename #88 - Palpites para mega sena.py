#88 - Palpites para mega sena
from random import randint
from time import sleep

jogos = list()
temp = list()
print('='*60)
print(f'{"JOGA NA MEGA SENA":^60}')
print('='*60)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    tot += 1
print('-='*10,f' SORTEANDO {quant} JOGOS', '-='*10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-='*11, '< BOA SORTE! >', '-='*11)
