#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep

n1 = float(input('Informe o primeiro número:'))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número:'))

print('-='*20)
print('Os números digitados foram: {}, {} e {}'.format(n1, n2, n3))

print('Analisando...')
sleep(3)

#vericando quem é maior

if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
        if n3 > n1 and n3 > n2:
            maior = n3

#verificando quem é menor

if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n1 and n2 < n3:
        menor = n2
    else:
        if n3 < n1 and n3 < n2:
            menor = n3


print("O maior entre ele é {} e o menor entre eles é {}".format(maior, menor))
