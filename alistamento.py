#alistamento
from time import sleep
from datetime import date
cores = {'green':'\033[1;32m',
         'red': '\033[1;31m',
         'yellow': '\033[1;33m',
         'limpa': '\033[m'} 

ano = int(input('QUAL ANO VOCÊ NASCEU? '))
hoje = date.today().year
print('ANALISANDO...')

if (hoje - ano) < 18:
    tempo = 18 - (hoje-ano)
    print('Você {}ainda vai se alistar{} ao serviço militar daqui {} anos'.format(cores['green'],cores['limpa'],tempo))
elif (hoje - ano) == 18:
    print('Esta na {}hora de se alistar{}'.format(cores['yellow'], cores['limpa']))
else:
    tempo = (hoje - ano) - 18
    print('Ja {}passou da hora{} do seu alistamento, deveria ter sido feito à {} anos atras'.format(cores['red'], cores['limpa'], tempo))