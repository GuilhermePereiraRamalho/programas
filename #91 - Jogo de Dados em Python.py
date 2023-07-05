#91 - Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogada = dict()
ranking = list()

for c in range(0,4):
    jogada[f'Jogador{c+1}'] = randint(1,6)   
print('Valores sorteados: ')
for k, v in jogada.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(.5)
print('-='*30)
print(' == Raking dos jogadores == ')
ranking = sorted(jogada.items(), key = itemgetter(1), reverse = True)
for k, v in enumerate(ranking):
    print(f'  {k+1}ºlugar: {v[0]} com {v[1]}')
    sleep(.5)

