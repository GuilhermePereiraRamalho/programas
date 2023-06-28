#41 - Categoria natação
from time import sleep
cores = {'blue': '\033[1;34m', 'limpa': '\033[m'}

nome = input('Qual seu nome? ')
idade = int(input('{}, qual sua idadde? '.format(nome)))

print('ANALISANDO...')
sleep(3)

if idade < 9:
    print('{}, com {} anos você fazer parte da categoria {}MRIRM{}'.format(nome, idade, cores['blue'], cores['limpa']))
elif idade >= 9 and idade < 14:
    print('{}, com {} anos você fazer parte da categoria {}INFANTIL{}'.format(nome, idade, cores['blue'], cores['limpa']))
elif idade > 14 and idade < 19:  
    print('{}, com {} anos você fazer parte da categoria {}JUNIOR{}'.format(nome, idade, cores['blue'], cores['limpa']))
elif idade >= 19 and idade <20:
    print('{}, com {} anos você fazer parte da categoria {}SENIOR{}'.format(nome, idade, cores['blue'], cores['limpa']))  
else:
    print('{}, com {} anos você fazer parte da categoria {}MASTER{}'.format(nome, idade, cores['blue'], cores['limpa']))