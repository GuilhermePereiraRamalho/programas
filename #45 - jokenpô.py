#45 - jokenpô
from random import choice
from time import sleep
cores = {'red': '\033[1;31m',
         'yellow': '\033[1;33m',
         'green': '\033[1;32m',
         'limpa': '\033[m'}

#seleção computador

esc_pc = choice(['Pedra', 'Papel', 'Tesoura'])

#seleção usuário

print('='*12)
print('  JOKENPÔ  ')
print('='*12)

print('''1 - Pedra
2 - Papel
3 - Tesoura ''')
esc = int(input('Selecione uma opção: '))
print('Jo')
sleep(.5)
print('Ken')
sleep(.5)
print('Pô')
sleep(.5)
if esc == 1:
    if esc_pc == 'Pedra':
        print('O computador também escolheu Pedra, vocês {}empataram!{}'.format(cores['yellow'],cores['limpa']))
    elif esc_pc == 'Papel':
        print('O computador escolheu Papel, você {}perdeu{}'.format(cores['red'], cores['limpa']))
    elif esc_pc == 'Tesoura':
        print('O computador escolheu Tesoura, você {}ganhou!!!{}'.format(cores['green'], cores['limpa']))
elif esc == 2:
    if esc_pc == 'Pedra':
        print('O computador escolheu Pedra, você {}ganhou!!!{}'.format(cores['green'], cores['limpa']))
    elif esc_pc == 'Papel':
        print('O computador também escolheu Papel, vocês {}empataram!{}'.format(cores['yellow'],cores['limpa']))
    elif esc_pc == 'Tesoura':
        print('O computador escolheu Tesoura, você {}perdeu{}'.format(cores['red'], cores['limpa']))
else:
    if esc_pc == 'Pedra':
        print('O computador escolheu Pedra, você {}perdeu{}'.format(cores['red'], cores['limpa']))
    elif esc_pc == 'Papel':
        print('O computador escolheu Papel, você {}ganhou!!!{}'.format(cores['green'], cores['limpa']))
    elif esc_pc == 'Tesoura':
        print('O computador também escolheu Tesoura, vocês {}empataram!{}'.format(cores['yellow'],cores['limpa']))