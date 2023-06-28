#Escreva um programa que leia um numero interio qualquer e peça para o usuário escolher qual sera a base de dados de conversão: 1 para binario 2 para octal e 3 para hexa
from time import sleep

cores = {'limpa' : '\033[m',
         'red' : '\033[1;31m',
         'green': '\033[1;32m',
         'blue': '\033[1;34m'}

#inicio
print('{}=={}'.format(cores['green'],cores['limpa']) *20)
print('          {}CONVERSOR DE NUMEROS{}      '.format(cores['green'],cores['limpa']))
print('{}=={}'.format(cores['green'],cores['limpa']) *20)

#input de dados
nome = input('{}QUAL SEU NOME?{}'.format(cores['green'],cores['limpa']))
n = int(input('{}{}, INFORME QUAL O NÚMERO QUE VOCÊ QUER CONVERTER: {}'.format(cores['green'],nome.upper(),cores['limpa'])))

#menu
print('{}=={}'.format(cores['blue'],cores['limpa']) *20)
print('          {}SELECIONE UMA OPÇÃO{}     '.format(cores['blue'],cores['limpa']))
print('{}=={}'.format(cores['blue'],cores['limpa']) *20)
print('''{}           1 - BINARIO
           2 - OCTAL
           3 - HEXADECIMAL{}'''.format(cores['blue'],cores['limpa']))

escolha = int(input('{} SUA ESCOLHA: '.format(cores['blue'],cores['limpa'])))

print('{}CONVERTENDO...{}'.format(cores['blue'],cores['limpa']))

sleep(3)
if escolha == 1:
     print('O número {}, convertido para binário é: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {}, convertido para octal é: {}'.format(n, oct(n)[2:]))
elif escolha ==3:
    print('O número {}, convertido para hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('{}OPÇÃO INVÁLIDA!!!{}'.format(cores['red'],cores['limpa']))