#43 - imc
from time import sleep

cores = {'limpa': '\033[m',
         'red': '\033[1;31m',
         'green': '\033[1;32m',
         'yellow': '\033[1;33m',
         'blue': '\033[1;34m'}

nome = input('Me informe seu nome: ')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

print('CALCULANDO...')
sleep(3)

imc = peso / (altura ** 2)

if imc < 18.5:
    print('{}, seu IMC é de {:=.2f}, e você está abaixo do peso'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print('{}, seu IMC é de {:=.2f}, e você está no {}peso ideal{}'.format(nome, imc, cores['green'], cores['limpa']))
elif imc >= 25 and imc < 30:
    print('{}, seu IMC é de {:=.2f}, e você está com {}sobrepeso{}'.format(nome, imc,cores['yellow'], cores['limpa']))
elif imc >= 30 and imc < 40:
    print('{}, seu IMC é de {:=.2f}, e você está com {}obesidade{}'.format(nome, imc, '\033[31m', cores['limpa']))
else:
    print('{}, seu IMC é de {:=.2f}, e você está com {}obesidade móbida{}'.format(nome, imc, cores['red'], cores['limpa']))