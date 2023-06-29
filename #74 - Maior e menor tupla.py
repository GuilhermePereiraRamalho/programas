#74 - Maior e menor tupla
from random import randint
v = (randint(0,10),randint(0,10),randint(0,10),
     randint(0,10),randint(0,10))
print('Os valores sorteados foram: ', end = '')
for i in v:
   print(f'{i} ', end = '')
print(f'\nO maior valor sorteado foi {max(v)}')
print(f'O menor valor sorteado foi {min(v)}')