#40 - calculo de média
from time import sleep
cores={'red': '\033[1;31m',
       'green': '\033[1;32m',
       'yellow': '\033[1;33m',
       'limpa': '\033[m'}

print('='*22)
print(' CALCULADORA DE MÉDIA')
print('='*22)

nome=input('Qual seu nome?')
n1 = float(input('{}, informe sua primeira nota: '.format(nome)))
n2 = float(input('{}, informe sua segunda nota: '.format(nome)))

print('CALCULANDO...')
sleep(3)

m = (n1 + n2)/2

if m<5:
    print('{}, sua média foi de {:=.1f}, aluno {}REPROVADO!!!{}'.format(nome,m,cores['red'],cores['limpa']))
elif m >= 5 and m < 7:
     print('{}, sua média foi de {:=.1f}, aluno {}EM RECUPERAÇÃO!!!{}'.format(nome,m,cores['yellow'],cores['limpa']))
else:
     print('{}, sua média foi de {:=.1f}, aluno {}APROVADO!!!{}'.format(nome,m,cores['green'],cores['limpa']))
