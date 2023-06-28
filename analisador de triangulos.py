# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep

print('-='*15)
print('   ANALISADOR DE TRIÂNGULOS   ')
print('-='*15)

s1 = float(input('Primeiro segumento: '))
s2 = float(input('Segundo Seguimento:'))
s3 = float(input('Terceiro Seguimento: '))
print('Analisando...')
sleep(3)
if (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')

