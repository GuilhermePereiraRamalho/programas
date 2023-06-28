## Um professor quer sortear um dos seus 4 alunos para apagar o quadro, faça um programa que leia o nome dos 4 e retorne o escolhido

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista=[n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))