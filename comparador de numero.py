#escreva um progama que leia dois numeros inteiros e compare-os, mostrando na tela ma msg
from time import sleep
#inicio
print('=='*20)
print('        COMPARADOR DE NUMEROS     ')
print('=='*20)

#input de dados
n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
print('COMPARANDO...')
sleep(3)

#body
if n1 > n2:
    print('O primeiro valor digitado é {}maior!{}'.format('\033[1;32m','\033[m'))
elif n2 > n1:
    print('O segundo valor digitado é {}maior!{}'.format('\033[1;32m','\033[m'))
else:
    print('Os dois são {}iguais!{}'.format('\033[1;32m','\033[m'))
    