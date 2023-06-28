#crie um programa que leia um numero inteiro e mostre se é par ou impar

n = int(input('Informe um número inteiro: '))

if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))